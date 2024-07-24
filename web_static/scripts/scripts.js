/*---------------Home page slide----------*/
let currentSlide = 0;
function showSlide(index) {
    
    const slides = document.querySelector('.opportunity-slider .opportunity-slide');
    const totalSlides = slides.children.length;
    const slideWidth = slides.children[1].offsetWidth + 20; // Including margin

    
    if (index >= totalSlides) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = 0;
    } else {
        currentSlide = index;
    }

    slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
    console.log(totalSlides)
}

function nextSlide() {
    showSlide(currentSlide + 3);
}

function prevSlide() {
    showSlide(currentSlide - 3);
}

function submitSignupForm(event) {
    event.preventDefault();

    const userType = document.getElementById('user-type').value

    if (userType === 'volunteer') {
        var fetchedUrl = 'http://localhost:5000/auth/volunteer-register'
        var formData = {
            first_name: document.getElementById('first_name').value,
            last_name: document.getElementById('last_name').value,
            email: document.getElementById('volunteer-email').value,
            password: document.getElementById('volunteer-password').value,
        };
    
    }

    if (userType === 'organization') {
        var fetchedUrl = 'http://localhost:5000/auth/organization-register'
        var formData = {
            org_name: document.getElementById('org-name').value,
            email: document.getElementById('org-email').value,
            password: document.getElementById('org-password').value,
        };
    }

    fetch(fetchedUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        alert('You have successfuly signed up. Please sign In to continue')
        console.log('sucess:', data);

        window.location.href = 'signin.html';
    })
    .catch(error => {
        alert('Error while trying to sign up')
        console.error('Error:', error);
    });
}

// Images for opportunity card

//---------------sign-in page-----------------
function submitSigninForm(event) {
    event.preventDefault();

    var formData = {
        email: document.getElementById('user-email').value,
        password: document.getElementById('user-password').value,
        };

    fetch('http://localhost:5000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {

        if(data.__class__){
            delete data.password;

            localStorage.setItem('userData', JSON.stringify(data));

            if(data.__class__ === 'Volunteer') {
                alert('Sign-in Succussful: you will be redirected to your dashboard');
                window.location.href = 'volunteer_dash.html';
            } else if (data.__class__ === 'Organization') {
                alert('Sign-in Succussful: you will be redirected to your dashboard');
                window.location.href = 'org_dash.html';
            }
        } else {
            alert('Invalid Login')
        }
    
    })
    .catch(error => {
        alert('Error while trying to sign in')
        console.error('Error:', error);
    });
}


//--------------------Sign-out function----------------------

function signOut() {

    window.localStorage.removeItem('userData');
    window.location.href = 'signin.html';
    /*fetch('http://localhost:5000/auth/logout', {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            localStorage.removeItem('userData');
            window.location.href = 'signin.html';
        } else {
            response.json().then(data => {
                console.error('Logout failed', data.message);
            });
        }
    })
    .catch(error => {
        console.error('Error:', error)
    });
    */
}

//-----------------vollunteer_dash page------------------------

document.addEventListener('DOMContentLoaded', () => {
    // This handles the view more functionality in the volunteer dashboard
    if (window.location.pathname.includes('volunteer_dash.html')) {
        const sections = document.querySelectorAll('.expandable-section');

        sections.forEach(section => {
            const title = section.querySelector('.section-title');
            title.addEventListener('click', () => {
                section.classList.toggle('expanded');
                sections.forEach(otherSection => {
                    if (otherSection !== section) {
                        otherSection.classList.remove('expanded');
                    }
                });
            });
        });

        document.addEventListener('click', (event) =>{
            if(event.target.classList.contains('view-details-btn')) {
                const applicationCard = event.target.closest('.application-card');
                applicationCard.classList.toggle('expanded');

                if (applicationCard.classList.contains('expanded')) {
                    event.target.textContent = 'View Less';
                } else {
                    event.target.textContent = 'View Details';
                }
            }
        });

    }

    // To load applications on page load
    if (window.location.pathname.includes('volunteer_dash.html')) {
        const applicationContainer = document.getElementById('applicationContainer');
        const applicationTemplate = document.querySelector('.application-card-template');
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userId = userData.id;

        fetch(`http://localhost:5000/applications/volunteer/${userId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                data.forEach(application => {
                    const applicationCard = applicationTemplate.cloneNode(true);
                    applicationCard.classList.remove('application-card-template');
                    applicationCard.style.display = 'block';

                    applicationCard.querySelector('.application-title').textContent = application.opp_title;
                    applicationCard.querySelector('.organization-name').textContent = application.org_name;
                    applicationCard.querySelector('.applied-date').textContent = new Date(application.created_at);
                    applicationCard.querySelector('.application-status').textContent = application.status;
                    applicationCard.querySelector('.application-description').textContent = application.opp_description;

                    const cancleButton = applicationCard.querySelector('.app-cancle-btn');
                    cancleButton.setAttribute('data-application-id', application.id);
                                        
                    applicationContainer.appendChild(applicationCard)
                });

                applicationContainer.addEventListener('click', (event) => {
                    if (event.target.classList.contains('app-cancle-btn')) {
                        const applicationId = event.target.dataset.applicationId;

                        fetch(`http://localhost:5000/applications/${applicationId}`, {
                            method: 'DELETE'
                        })
                        .then(response => {
                            if (response.ok) {
                                alert('You have canced this Application');
                                event.target.closest('.application-card').remove();
                            } else {
                                response.json().then(data => {
                                    console.log('Cancelation failed:', data.message);
                                });
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                    }
                });

            })
            .catch(error => {
                console.error('Error fetching applications', error);
            });
    }

});

// This is to edit and save volunteer's profile
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('volunteer_dash.html')) {
        const form = document.getElementById('volunteerProfileForm');
        const userData = JSON.parse(localStorage.getItem('userData'));

        form.addEventListener('submit', (event) => {
            event.preventDefault();

            const formatDate = (datastr) => {
                const [year, month, day] = datastr.split('-');
                return `${year}-${month}-${day}`
            };

            var formData = {
                first_name: document.getElementById('first_name').value,
                last_name: document.getElementById('last_name').value,
                gender: document.querySelector('input[name="gender"]:checked').value,
                date_of_birth: formatDate(document.getElementById('date_of_birth').value),
                phone_number: document.getElementById('phone_number').value,
                location: document.getElementById('location').value,
                skills: [],
                interests: [],
                availability: [],
                bio: document.getElementById('bio').value,    
            };

            document.querySelectorAll('input[name="skills"]:checked').forEach((checkbox) => {
                formData.skills.push(checkbox.nextSibling.textContent.trim());
            });

            document.querySelectorAll('input[name="interests"]:checked').forEach((checkbox) => {
                formData.interests.push(checkbox.nextSibling.textContent.trim());
            });

            document.querySelectorAll('input[name="availability"]:checked').forEach((checkbox) => {
                formData.availability.push(checkbox.nextSibling.textContent.trim());
            });

            //console.log(formData);

            fetch(`http://localhost:5000/volunteers/${userData.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                alert('profile updated successfully');
            })
            .catch((error) => {
                console.error('Error updating profile:', error);
                alert('Problem while updating profile, please try again');
            });
        });
    }
});




//--------------org_dash page---------------- 
// profile auto fill

document.addEventListener('DOMContentLoaded', () => {
    const currentPage = window.location.pathname;

    if (currentPage.includes('volunteer_dash.html')) {
        handleVolunteerDashboard();
    } else if (currentPage.includes('org_dash.html')) {
        handleOrganizationDashboard();
    }
});

function handleVolunteerDashboard() {
    const userData = JSON.parse(localStorage.getItem('userData'));
    const dateObj = new Date(userData.date_of_birth);
    const formatedDate = dateObj.toISOString().split('T')[0];
    //console.log(userData);

    if (userData && userData.__class__ === 'Volunteer') {
        document.getElementById('first_name').value = userData.first_name || '';
        document.getElementById('last_name').value = userData.last_name || '';
        document.getElementById('date_of_birth').value = formatedDate || '';
        document.getElementById('phone_number').value = userData.phone_number || '';
        document.getElementById('location').value = userData.location || '';
        document.getElementById('bio').value = userData.bio || '';

        if (userData.gender === 'male') {
            document.getElementById('male').checked = true;
        } else if (userData.gender === 'female') {
            document.getElementById('female').checked = true;
        }

        console.log(userData.interests);
        console.log(userData.skills);
        console.log(userData.availability);

        userData.interests.forEach(interest => {
            const interestCheckbox = document.querySelector(`input[name="interests"][value="${interest}"]`);
            if(interestCheckbox) {
                interestCheckbox.checked = true;
            }
        });

        userData.skills.forEach(skill => {
            const skillCheckbox = document.querySelector(`input[name="skills"][value="${skill}"]`);
            if(skillCheckbox) {
                skillCheckbox.checked = true;
            }
        });

        userData.availability.forEach(day => {
            const availabilityCheckbox = document.querySelector(`input[name="availability"][value="${day}"]`);
            if(availabilityCheckbox) {
                availabilityCheckbox.checked = true;
            }
        });

    }
}

function handleOrganizationDashboard() {
    const userData = JSON.parse(localStorage.getItem('userData'));
    const dateObj = new Date(userData.est_date);
    const formatedDate = dateObj.toISOString().split('T')[0];

    if (userData && userData.__class__ === 'Organization') {
        document.getElementById('org_name').value = userData.org_name || '';
        document.getElementById('est_date').value = formatedDate || '';
        document.getElementById('contact-email').value = userData.contact_email || '';
        document.getElementById('contact-phone').value = userData.contact_phone || '';
        document.getElementById('location').value = userData.location || '';
        document.getElementById('mission-statement').value = userData.mission_statement || '';
        document.getElementById('web-url').value = userData.website_url || '';
    }
}


// organization dashboard view more and view less functionality
document.addEventListener('DOMContentLoaded', () => {

    if (window.location.pathname.includes('org_dash.html')) {
        //const viewDetailsButtons = document.querySelectorAll('.view-details-btn');

        document.addEventListener('click', (event) =>{
            if(event.target.classList.contains('show-applicants')) {
                const postCard = event.target.closest('.post-card');
                postCard.classList.toggle('expanded');

                if (postCard.classList.contains('expanded')) {
                    event.target.textContent = 'Hide Applicants';
                } else {
                    event.target.textContent = 'View Applicants';
                }
            }
        });

        const sections = document.querySelectorAll('.expandable-section');

        sections.forEach(section => {
            const title = section.querySelector('.section-title');
            title.addEventListener('click', () => {
                section.classList.toggle('expanded');
                sections.forEach(otherSection => {
                    if (otherSection !== section) {
                        otherSection.classList.remove('expanded');
                    }
                });
            });
        });

        document.addEventListener('click', (event) => {
            if (event.target.classList.contains('show-applicants')) {
                const postCard = event.target.closest('.post-card');
                const applicantsContainer = postCard.querySelector('.applicant-container');

                if (!applicantsContainer) {
                    console.error('Applicants container not found');
                    return;
                }

                
                const header = applicantsContainer.querySelector('.applicant-header');
                const template = applicantsContainer.querySelector('.applicant-card-template');

                if (!template) {
                    console.error('Applicant card template not found');
                    return;
                }

                applicantsContainer.innerHTML = '';
                if (header) applicantsContainer.appendChild(header);
                if (template) applicantsContainer.appendChild(template);

                const postId = event.target.getAttribute('data-post-id');

                // Fetch applicants for the post
                fetch(`http://localhost:5000/applications/opportunity/${postId}`)
                    .then(response => response.json())
                    .then(applicants => {
                        if (applicants.length > 0) {
                            applicants.forEach(applicant => {
                                const applicantCard = template.cloneNode(true);
                                applicantCard.classList.remove('applicant-card-template');
                                //applicantCard.style.display = 'block';
                                applicantCard.querySelector('.applicant-name').textContent = applicant.volunteer_name;
                                applicantCard.querySelector('.application-date').textContent = new Date(applicant.created_at).toLocaleDateString();
                                applicantCard.querySelector('.show-profile-btn').setAttribute('data-application-id', applicant.id);
                                applicantCard.querySelector('.show-profile-btn').setAttribute('data-applicant-id', applicant.volunteer_id);
                                applicantsContainer.appendChild(applicantCard);
                            });
                        } else {
                            const noApplicantsMessage = document.createElement('p');
                            noApplicantsMessage.textContent = 'No applicants found.';
                            applicantsContainer.appendChild(noApplicantsMessage);
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching applicants', error);
                        const errorMessage = document.createElement('p');
                        errorMessage.textContent = 'Error fetching applicants.';
                        applicantsContainer.appendChild(errorMessage);
                    });
            }
        });

    }

    //To load opportunities when the org_dash loads
    if (window.location.pathname.includes('org_dash.html')) {
        const postContainer = document.getElementById('postContainer');
        const postTemplate = document.querySelector('.post-card-template');
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userId = userData.id;

        fetch(`http://localhost:5000/opportunities/organization/${userId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                data.forEach(post => {
                    const postCard = postTemplate.cloneNode(true);
                    postCard.classList.remove('post-card-template');
                    postCard.style.display = 'block';

                    postCard.querySelector('.post-title').textContent = post.title;
                    postCard.querySelector('.organization-name').textContent = post.org_name;
                    postCard.querySelector('.post-start-date').textContent = new Date(post.start_date);
                    postCard.querySelector('.post-end-date').textContent = new Date(post.end_date);
                    
                    //postCard.querySelector('.post-description').textContent = post.description;

                    const showButton = postCard.querySelector('.show-applicants');
                    showButton.setAttribute('data-post-id', post.id);
                                        
                    postContainer.appendChild(postCard)
                });
            })
            .catch(error => {
                console.error('Error fetching posts', error);
            });
    }

});


// organization dashboard creating new post
document.addEventListener('DOMContentLoaded', () => {
    if(window.location.pathname.includes('org_dash.html')) {

        const form = document.getElementById('postingForm');
        const userData = JSON.parse(localStorage.getItem('userData'));

        form.addEventListener('submit', (event) => {
            event.preventDefault();

            const formatDate = (datastr) => {
                const [year, month, day] = datastr.split('-');
                return `${year}-${month}-${day}`
            };

            var formData = {
                org_id: userData.id,
                org_name: userData.org_name,
                title: document.getElementById('post-title').value,
                opp_type: document.getElementById('post-type').value,
                description: document.getElementById('postDescription').value,
                skills_required: [],
                interests_required: [],
                start_date: formatDate(document.getElementById('startingDate').value),
                end_date: formatDate(document.getElementById('endingDate').value),
                location: document.getElementById('post-location').value
            };

            document.querySelectorAll('input[name="skills"]:checked').forEach((checkbox) => {
                formData.skills_required.push(checkbox.value);
            });

            document.querySelectorAll('input[name="interests"]:checked').forEach((checkbox) => {
                formData.interests_required.push(checkbox.value);
            });

            //console.log(formData);

            fetch('http://127.0.0.1:5000/opportunities', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                alert('Opportunity Posted')
                form.reset();
            })
            .catch((error) => {
                alert('Problem while posting, Retry');
            });
        });

    }
        
});

// This is to save and edit organization's profile
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('org_dash.html')) {
        const form = document.getElementById('organizationProfileForm');
        const userData = JSON.parse(localStorage.getItem('userData'));
        console.log(userData);

        form.addEventListener('submit', (event) => {
            event.preventDefault();

            const formatDate = (datastr) => {
                const [year, month, day] = datastr.split('-');
                return `${year}-${month}-${day}`
            };

            var formData = {
                org_name: document.getElementById('org_name').value,
                est_date: formatDate(document.getElementById('est_date').value),
                mission_statement: document.getElementById('mission-statement').value,
                contact_email: document.getElementById('contact-email').value,
                contact_phone: document.getElementById('contact-phone').value,
                location: document.getElementById('location').value,
                website_url: document.getElementById('web-url').value
            };

            //console.log(formData);
            //alert('data created');

            fetch(`http://localhost:5000/organizations/${userData.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                alert('profile updated successfully');
            })
            .catch((error) => {
                console.error('Error updating profile:', error);
                alert('Problem while updating profile, please try again');
            });
            
        });
    }
});

//----------------OPPORTUNITIES PAGE----------------

document.addEventListener('DOMContentLoaded', () => {
    if(window.location.pathname.includes('opportunities.html')) {
        document.addEventListener('click', (event) =>{
            if(event.target.classList.contains('view-details-btn')) {
                const opportunityCard = event.target.closest('.opportunity-card');
                opportunityCard.classList.toggle('expanded');

                if (opportunityCard.classList.contains('expanded')) {
                    event.target.textContent = 'View Less';
                } else {
                    event.target.textContent = 'View Details';
                }
            }
        });
    }
});

//------------------Filtering opportunities----------------------

document.addEventListener('DOMContentLoaded', () => {

    function loadOpportunities() {
        const opportunityContainer = document.getElementById('opportunityContainer');
        const opportunityTemplate = document.querySelector('.opportunity-card-template');

        const location = document.querySelector('input[name="location"]').value;
        const startDate = document.querySelector('input[name="startDate"]').value;
        const type = document.querySelector('select[name="type"]').value;

        

        if(!opportunityTemplate) {
            console.error('opportunity template not found')
        }

        opportunityContainer.innerHTML = '';

        const queryParams = new URLSearchParams();
        if (location) queryParams.append('location', location);
        if (startDate) queryParams.append('startDate', startDate);
        if (type) queryParams.append('type', type);

        fetch(`http://localhost:5000/opportunities?${queryParams.toString()}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                data.forEach(opportunity => {
                    const opportunityCard = opportunityTemplate.cloneNode(true);
                    opportunityCard.classList.remove('opportunity-card-template');
                    opportunityCard.style.display = 'block';

                    opportunityCard.querySelector('.opportunity-title').textContent = opportunity.title;
                    opportunityCard.querySelector('.organization-name').textContent = opportunity.org_name;
                    opportunityCard.querySelector('.starting-date').textContent = new Date(opportunity.start_date);
                    opportunityCard.querySelector('.ending-date').textContent = new Date(opportunity.end_date);
                    opportunityCard.querySelector('.opportunity-type').textContent = opportunity.opp_type;
                    opportunityCard.querySelector('.opportunity-description').textContent = opportunity.description;
                    opportunityCard.querySelector('.skills-needed').textContent = opportunity.skills_required.join(', ');
                    opportunityCard.querySelector('.interest-needed').textContent = opportunity.interests_required.join(', ');
                    opportunityCard.querySelector('.location').textContent = opportunity.location;

                    const applyButton = opportunityCard.querySelector('.apply-btn');
                    applyButton.setAttribute('data-opportunity-id', opportunity.id);
                    applyButton.setAttribute('data-opportunity-org', opportunity.org_name);
                    applyButton.setAttribute('data-opportunity-title', opportunity.title);
                    applyButton.setAttribute('data-opportunity-description', opportunity.description);
                                        
                    opportunityContainer.appendChild(opportunityCard)
                });
            })
            .catch(error => {
                console.error('Error fetching opportunities', error);
            });

    }

    if (window.location.pathname.includes('opportunities.html')) {
        loadOpportunities();
    }

    const filterForm = document.getElementById('filterForm');
    if (filterForm) {
        filterForm.addEventListener('submit', (event) => {
            event.preventDefault();
            loadOpportunities();
        });
    }
});



//----------------Appliying to opportunity-------------------
document.addEventListener('click', (event) => {
    if (event.target.classList.contains('apply-btn')) {
        const opportunityId = event.target.dataset.opportunityId;
        const opportunityOrg = event.target.dataset.opportunityOrg;
        const opportunityTitle = event.target.dataset.opportunityTitle;
        const opportunityDescription = event.target.dataset.opportunityDescription;
        const userData = JSON.parse(localStorage.getItem('userData'));
        
        if (!userData) {
            alert('Please sign in before you can apply')
            redirectPage('signin.html');
            return;
        }

        if (userData.__class__ === 'Organization') {
            alert('Organizations can not apply to an opportunity')
        } 
        if (userData.__class__ === 'Volunteer') {
            const userId = userData.id;
            const userName = userData.first_name;
            //console.log(opportunityId);
            //console.log(userId);

            fetch('http://localhost:5000/applications', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({opportunity_id: opportunityId, org_name: opportunityOrg, opp_title: opportunityTitle, opp_description: opportunityDescription, volunteer_id: userId, volunteer_name: userName})
            })
            .then(response => {
                if (response.ok) {
                    alert('Successfuly applied to this post');
                } else {
                    response.json().then(data => {
                        console.error('Application failed:', data.message);
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
        
    }
});

function redirectPage(url) {
    window.location.href = url;
}


// organization dash, volunteer profile view

document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('org_dash.html')) {
        document.body.addEventListener('click', async (event) => {
            if (event.target.classList.contains('show-profile-btn')) {
                console.log('Button clicked');
                const volunteerId = event.target.getAttribute('data-applicant-id');
                const applicationId = event.target.getAttribute('data-application-id');
                
                try {
                    const response = await fetch(`http://localhost:5000/volunteers/${volunteerId}`);
                    if (!response.ok) throw new Error('Network response was not ok');
                    
                    const profile = await response.json();
                    console.log('Profile fetched:', profile);
                    
                    showProfilePopup(profile, applicationId);
                } catch (error) {
                    console.error('Error fetching profile:', error);
                    alert('An error occurred while fetching the profile.');
                }
            }
        });
    }
});

function showProfilePopup(profile, applicationId) {
    const popup = document.createElement('div');
    popup.innerHTML = `
        <div style="
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 400px;
            background: white;
            border: 1px solid #ddd;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        ">
            <h2>${profile.first_name} ${profile.last_name}</h2>
            <p><strong>Gender:</strong> ${profile.gender}</p>
            <p><strong>Date of Birth:</strong> ${profile.date_of_birth}</p>
            <p><strong>Phone Number:</strong> ${profile.phone_number}</p>
            <p><strong>Location:</strong> ${profile.location}</p>
            <p><strong>Skills:</strong> ${profile.skills.join(', ')}</p>
            <p><strong>Interests:</strong> ${profile.interests.join(', ')}</p>
            <p><strong>Availability:</strong> ${profile.availability}</p>
            <p><strong>Bio:</strong> ${profile.bio}</p>
            <button style="
                position: absolute;
                top: 10px;
                right: 10px;
                background: #f00;
                color: #fff;
                border: none;
                padding: 5px 10px;
                cursor: pointer;
            ">Close</button>
            <div style="
                margin-top: 20px;
                text-align: center;
            ">
                <button class="accept-btn" style="
                    background: #0f0;
                    color: #fff;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                ">Accept</button>
                <button class="reject-btn" style="
                    background: #f00;
                    color: #fff;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                ">Reject</button>
            </div>
        </div>
    `;

    document.body.appendChild(popup);
    
    popup.querySelector('button').addEventListener('click', () => {
        document.body.removeChild(popup);
    });

    // Add event listeners for Accept and Reject buttons
    popup.querySelector('.accept-btn').addEventListener('click', () => {
        updateApplicationStatus(applicationId, 'Accepted');
        document.body.removeChild(popup);
    });

    popup.querySelector('.reject-btn').addEventListener('click', () => {
        updateApplicationStatus(applicationId, 'Rejected');
        document.body.removeChild(popup);
    });
}

async function updateApplicationStatus(applicationId, status) {
    try {
        const response = await fetch(`http://localhost:5000/applications/${applicationId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ status: status }),
        });

        if (!response.ok) throw new Error('Network response was not ok');
        
        const result = await response.json();
        console.log('Application status updated:', result);
        alert(`Application ${status}`);
    } catch (error) {
        console.error('Error updating application status:', error);
        alert('An error occurred while updating the application status.');
    }
}
