  // Mock data representing children's progress
  const childrenData = [
    {
        id: 1,
        name: 'Andi Prasetyo',
        age: 4,
        foto: 'https://via.placeholder.com/100',
        perkembangan: [
            {
                kategori: 'Sosial Emosional',
                deskripsi: 'Mulai berkembang kemampuan berinteraksi dengan teman sebaya',
                tingkat: 'Berkembang Sesuai Harapan'
            },
            {
                kategori: 'Kognitif',
                deskripsi: 'Mampu mengenal warna dan bentuk dasar dengan baik',
                tingkat: 'Berkembang Sangat Baik'
            },
            {
                kategori: 'Motorik',
                deskripsi: 'Koordinasi gerak mulai meningkat, dapat menggunting dengan bantuan',
                tingkat: 'Berkembang Sesuai Harapan'
            }
        ]
    },
    {
        id: 2,
        name: 'Budi Santoso',
        age: 5,
        foto: 'https://via.placeholder.com/100',
        perkembangan: [
            {
                kategori: 'Sosial Emosional',
                deskripsi: 'Sudah mandiri dan dapat berbagi dengan teman',
                tingkat: 'Berkembang Sangat Baik'
            },
            {
                kategori: 'Kognitif',
                deskripsi: 'Mampu berhitung sederhana dan mengenal huruf',
                tingkat: 'Berkembang Sangat Baik'
            },
            {
                kategori: 'Bahasa',
                deskripsi: 'Komunikasi lancar dan dapat menceritakan pengalaman',
                tingkat: 'Berkembang Sangat Baik'
            }
        ]
    }
];

// Function to get color based on development level
function getTingkatColor(tingkat) {
    switch(tingkat) {
        case 'Berkembang Sangat Baik': 
            return 'level-very-good';
        case 'Berkembang Sesuai Harapan': 
            return 'level-expected';
        default: 
            return '';
    }
}

// Function to get icon for development category
function getCategoryIcon(kategori) {
    const icons = {
        'Sosial Emosional': '😊',
        'Kognitif': '📖',
        'Motorik': '🏃',
        'Bahasa': '💬'
    };
    return icons[kategori] || '📝';
}

// Render children selection
function renderChildrenSelection() {
    const childSelection = document.getElementById('child-selection');
    childrenData.forEach(child => {
        const childCard = document.createElement('div');
        childCard.className = 'child-card';
        childCard.dataset.childId = child.id;
        childCard.innerHTML = `
            <img src="${child.foto}" alt="${child.name}">
            <span class="child-name">${child.name}</span>
            <span class="child-age">${child.age} tahun</span>
        `;
        childCard.addEventListener('click', () => selectChild(child));
        childSelection.appendChild(childCard);
    });
}

// Select child and show development details
function selectChild(child) {
    // Reset previous selection
    document.querySelectorAll('.child-card').forEach(card => {
        card.classList.remove('selected');
    });

    // Highlight selected child
    const selectedCard = document.querySelector(`.child-card[data-child-id="${child.id}"]`);
    selectedCard.classList.add('selected');

    // Show development details
    const developmentDetails = document.getElementById('development-details');
    const developmentTitle = document.getElementById('development-title');
    const developmentList = document.getElementById('development-list');

    developmentTitle.textContent = `Detail Perkembangan ${child.name}`;
    
    // Clear previous details
    developmentList.innerHTML = '';

    // Render development items
    child.perkembangan.forEach(item => {
        const developmentItem = document.createElement('div');
        developmentItem.className = 'development-item';
        developmentItem.innerHTML = `
            <div class="development-icon">${getCategoryIcon(item.kategori)}</div>
            <div class="development-content">
                <div class="development-category">${item.kategori}</div>
                <div class="development-description">${item.deskripsi}</div>
                <span class="development-level ${getTingkatColor(item.tingkat)}">
                    ${item.tingkat}
                </span>
            </div>
        `;
        developmentList.appendChild(developmentItem);
    });

    // Show development details
    developmentDetails.style.display = 'block';
}

// Initialize the page
function init() {
    renderChildrenSelection();
    
    // Automatically select first child
    if (childrenData.length > 0) {
        selectChild(childrenData[0]);
    }
}

// Run initialization when DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);
