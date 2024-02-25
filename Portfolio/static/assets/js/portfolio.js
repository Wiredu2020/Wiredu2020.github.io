
    document.addEventListener('DOMContentLoaded', function() {
        // Function to handle smooth scrolling to a section
        function scrollToSection(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                // Fallback to regular anchor behavior if the section is not found
                window.location.href = `index.html#${sectionId}`;
            }
        }

        // Get navbar links
        const aboutLink = document.getElementById('aboutLink');
        const resumeLink = document.getElementById('resumeLink');
        const portfolioLink = document.getElementById('portfolioLink');
        const servicesLink = document.getElementById('servicesLink');

        // Add click event listeners to navbar links
        if (aboutLink) {
            aboutLink.addEventListener('click', function(event) {
                event.preventDefault();
                scrollToSection('about');
            });
        }
        if (resumeLink) {
            resumeLink.addEventListener('click', function(event) {
                event.preventDefault();
                scrollToSection('resume');
            });
        }
        if (portfolioLink) {
            portfolioLink.addEventListener('click', function(event) {
                event.preventDefault();
                scrollToSection('portfolio');
            });
        }
        if (servicesLink) {
            servicesLink.addEventListener('click', function(event) {
                event.preventDefault();
                scrollToSection('services');
            });
        }
    });

