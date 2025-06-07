// Navigation Header for The Free Korean Website
// This script automatically injects navigation header into all pages

document.addEventListener('DOMContentLoaded', function() {
    // Create the navigation header HTML
    const headerHTML = `
        <!-- Navigation Header -->
        <header class="bg-white shadow-lg sticky top-0 z-50 mb-6">
            <div class="container mx-auto px-6 py-4">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
                            <span class="text-white font-bold" style="font-family: 'Noto Sans KR', sans-serif;">한</span>
                        </div>
                        <div>
                            <a href="index.html" class="text-2xl font-bold text-gray-900 hover:text-blue-600 transition-colors">The Free Korean</a>
                            <p class="text-sm text-gray-600">Học tiếng Hàn miễn phí</p>
                        </div>
                    </div>
                    <nav class="hidden md:flex space-x-6">
                        <a href="index.html" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-1">
                            <i class="fas fa-home"></i>
                            <span>Trang chủ</span>
                        </a>
                        <a href="index.html#lessons" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-1">
                            <i class="fas fa-book"></i>
                            <span>Tất cả bài học</span>
                        </a>
                        <a href="index.html#posts" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-1">
                            <i class="fas fa-newspaper"></i>
                            <span>Tin tức</span>
                        </a>
                    </nav>
                    <button class="md:hidden text-gray-700" onclick="toggleMobileMenu()">
                        <i class="fas fa-bars text-xl"></i>
                    </button>
                </div>
                <!-- Mobile Menu -->
                <div id="mobile-menu" class="md:hidden mt-4 pb-4 border-t border-gray-200 hidden">
                    <div class="flex flex-col space-y-3 pt-4">
                        <a href="index.html" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-2">
                            <i class="fas fa-home"></i>
                            <span>Trang chủ</span>
                        </a>
                        <a href="index.html#lessons" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-2">
                            <i class="fas fa-book"></i>
                            <span>Tất cả bài học</span>
                        </a>
                        <a href="index.html#posts" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center space-x-2">
                            <i class="fas fa-newspaper"></i>
                            <span>Tin tức</span>
                        </a>
                    </div>
                </div>
            </div>
        </header>
    `;

    // Find the body element and insert header at the beginning
    const body = document.body;
    if (body) {
        body.insertAdjacentHTML('afterbegin', headerHTML);
    }

    // Add breadcrumb navigation to page titles (except index.html)
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage !== 'index.html' && currentPage !== '') {
        addBreadcrumbNavigation();
    }

    // Load Font Awesome if not already loaded
    if (!document.querySelector('link[href*="font-awesome"]')) {
        const fontAwesome = document.createElement('link');
        fontAwesome.rel = 'stylesheet';
        fontAwesome.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css';
        document.head.appendChild(fontAwesome);
    }
});

// Mobile menu toggle function
window.toggleMobileMenu = function() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        if (mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.remove('hidden');
        } else {
            mobileMenu.classList.add('hidden');
        }
    }
};

// Add breadcrumb navigation to page headers
function addBreadcrumbNavigation() {
    const pageMapping = {
        'Nguyên âm - TEST.html': 'Ôn tập nguyên âm',
        'Phụ âm thường - LUYỆN TẬP.html': 'Luyện tập phụ âm thường',
        'Phụ âm bật hơi - LUYỆN TẬP.html': 'Luyện tập phụ âm bật hơi',
        'Phụ âm căng - LUYỆN TẬP.html': 'Luyện tập phụ âm căng',
        'Phụ âm - LUYỆN TẬP.html': 'Luyện tập phụ âm',
        'Phụ âm - LUYỆN TẬP 1.html': 'Luyện tập phụ âm 1'
    };

    const currentPage = window.location.pathname.split('/').pop();
    const pageName = pageMapping[currentPage] || 'Bài học';

    // Find the main header (h1) and add breadcrumb after it
    const mainHeader = document.querySelector('h1');
    if (mainHeader && !document.querySelector('.breadcrumb-nav')) {
        const breadcrumbHTML = `
            <div class="breadcrumb-nav flex items-center justify-center mt-4 space-x-4 text-sm text-gray-600">
                <a href="index.html" class="hover:text-blue-600 transition-colors">Trang chủ</a>
                <span>›</span>
                <a href="index.html#lessons" class="hover:text-blue-600 transition-colors">Bài học</a>
                <span>›</span>
                <span class="text-blue-600 font-semibold">${pageName}</span>
            </div>
        `;
        mainHeader.insertAdjacentHTML('afterend', breadcrumbHTML);
    }
}
