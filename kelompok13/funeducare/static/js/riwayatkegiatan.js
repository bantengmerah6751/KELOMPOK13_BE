document.addEventListener('DOMContentLoaded', function() {
    const activityContainer = document.getElementById('activityContainer');
    const filterButtons = document.querySelectorAll('.filter-btn');
    let activities = []; // Data kegiatan dari API

    // Fungsi untuk mengambil data kegiatan dari API
    async function fetchActivities() {
        try {
            const response = await fetch('/api/kegiatan/');
            activities = await response.json();
            renderActivities('all');
        } catch (error) {
            console.error('Gagal mengambil data:', error);
            activityContainer.innerHTML = '<p>Gagal memuat aktivitas</p>';
        }
    }

    // Fungsi untuk mendapatkan ikon berdasarkan jenis kegiatan
    function getActivityIcon(jenis) {
        const icons = {
            'makan': '🍽️',
            'bermain': '🏀',
            'tidur': '😴',
            'belajar': '📚'
        };
        return icons[jenis] || '📝';
    }

    // Fungsi untuk mendapatkan warna berdasarkan jenis kegiatan
    function getActivityColor(jenis) {
        const colors = {
            'makan': '#2ecc71',
            'bermain': '#3498db',
            'tidur': '#9b59b6',
            'belajar': '#f39c12'
        };
        return colors[jenis] || '#34495e';
    }

    // Fungsi untuk merender aktivitas
    function renderActivities(filter) {
        activityContainer.innerHTML = ''; // Bersihkan kontainer

        const filteredActivities = filter === 'all' 
            ? activities 
            : activities.filter(activity => activity.jenis === filter);

        if (filteredActivities.length === 0) {
            activityContainer.innerHTML = '<p>Tidak ada aktivitas ditemukan</p>';
            return;
        }

        filteredActivities.forEach(activity => {
            const activityItem = document.createElement('article');
            activityItem.classList.add('activity-item');
            
            activityItem.innerHTML = `
                <div class="activity-icon" style="background-color: ${getActivityColor(activity.jenis)}">
                    ${getActivityIcon(activity.jenis)}
                </div>
                <div class="activity-details">
                    <h3>${activity.nama_anak}</h3>
                    <p>${activity.jenis.charAt(0).toUpperCase() + activity.jenis.slice(1)} - ${activity.waktu}</p>
                    <p>${activity.deskripsi}</p>
                </div>
            `;

            activityContainer.appendChild(activityItem);
        });
    }

    // Event listener untuk filter
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            renderActivities(button.dataset.filter);
        });
    });

    // Panggil fungsi fetch saat halaman dimuat
    fetchActivities();
});
