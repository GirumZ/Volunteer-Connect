let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelector('.opportunity-slider .opportunity-slide');
    const totalSlides = slides.children.length;
    const slideWidth = slides.children[0].offsetWidth + 20; // Including margin

    if (index >= totalSlides) {
        currentSlide = totalSlides - 1;
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

/*function showNotification(message) {
    var notificationContainer = document.getElementById('notificationContainer');

    var notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;

    notificationContainer.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('show');
    }, 100);

    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notificationContainer.removeChild(notification);
        },500);
    }, 3000);
}
*/

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