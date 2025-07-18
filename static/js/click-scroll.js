// Enhanced click-scroll handler with complete error protection
document.addEventListener('DOMContentLoaded', function() {
    // Handle click events
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('click-scroll')) {
            e.preventDefault();
            var target = e.target.getAttribute('href');
            
            // Only process anchor links
            if (target && target.startsWith('#')) {
                try {
                    var targetElement = document.querySelector(target);
                    if (targetElement) {
                        var offset = targetElement.getBoundingClientRect().top + window.pageYOffset - 90;
                        window.scrollTo({
                            top: offset,
                            behavior: 'smooth'
                        });
                        
                        // Update URL without page reload
                        if (history.pushState) {
                            history.pushState(null, null, target);
                        } else {
                            window.location.hash = target;
                        }
                    } else {
                        console.warn('Target element not found:', target);
                        window.location.href = target; // Fallback
                    }
                } catch (error) {
                    console.error('Scroll error:', error);
                    window.location.href = target; // Fallback
                }
            }
        }
    });

    // Handle initial page load with hash
    if (window.location.hash) {
        setTimeout(function() {
            try {
                var targetElement = document.querySelector(window.location.hash);
                if (targetElement) {
                    var offset = targetElement.getBoundingClientRect().top + window.pageYOffset - 90;
                    window.scrollTo({
                        top: offset,
                        behavior: 'smooth'
                    });
                }
            } catch (error) {
                console.error('Initial scroll error:', error);
            }
        }, 100);
    }
});