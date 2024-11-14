// sign up

$(document).ready(function () {
  // Fungsi untuk menampilkan modal

  function showModal() {
    $("#loginSuccessModal").fadeIn(); // Menggunakan fadeIn() untuk efek muncul modal
  }

  // Menutup modal jika pengguna mengklik di luar modal
  $(window).on("click", function (event) {
    if ($(event.target).is("#loginSuccessModal")) {
      $("#loginSuccessModal").fadeOut(); // Menutup modal dengan fadeOut
    }
  });

  // Event listener untuk form submit
  $("#signinForm").on("submit", function (event) {
    event.preventDefault(); // Mencegah form dari pengiriman default
    showModal(); // Menampilkan modal
  });

  // Menutup modal hanya jika tombol OK diklik
  $(".close-btn").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman index.html
    window.location.href = "login.html"; // Pindah ke halaman index.html
  });
});
