// scroll explore
$(document).ready(function () {
  $("#scrollButton").on("click", function (event) {
    event.preventDefault();
    $("html, body").animate(
      {
        scrollTop: $("#marqueForm").offset().top,
      },
      1500
    );
  });
});

$(document).ready(function () {
  const readMoreButtons = [
    "readMoreBtn1",
    "readMoreBtn2",
    "readMoreBtn3",
    "readMoreBtn4",
    "readMoreBtn5",
    "readMoreBtn6",
  ];

  readMoreButtons.forEach((buttonId) => {
    $(`#${buttonId}`).on("click", function () {
      const index = buttonId.charAt(buttonId.length - 1);
      const $dots = $(`#dots${index}`);
      const $moreText = $(`#more${index}`);

      const isExpanded = $moreText.css("display") === "inline";

      if (isExpanded) {
        $dots.css("display", "inline");
        $moreText.css("display", "none");
        $(this).text("Tampilkan lebih banyak");
      } else {
        $dots.css("display", "none");
        $moreText.css("display", "inline");
        $(this).text("Sembunyikan");
      }
    });
  });
});

// back to top
$(document).ready(function () {
  // Menampilkan atau menyembunyikan tombol saat menggulir
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $("#backToTop").fadeIn(); // Tampilkan tombol
    } else {
      $("#backToTop").fadeOut(); // Sembunyikan tombol
    }
  });

  // logic klik pada tombol
  $("#backToTop").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500); // Menggunakan animasi
  });
});

// animasi pop up formwali
$(document).ready(function () {
  $("#getStarted").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal").modal("show");
  });

  $("#waliForm").on("submit", function (event) {
    event.preventDefault(); // Mencegah form dari pengiriman default
    showModal(); // Menampilkan modal
  });
  // Menutup modal hanya jika tombol OK diklik
  $(".close").on("click", function () {
    $("#verificationModal").modal("hide");
  });
  $(".close-btn").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
    window.location.href = "login.html"; // Pindah ke halaman homepage.html
  });
  $(".close-btn2").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
    window.location.href = "dashboard.html"; // Pindah ke halaman homepage.html
  });
});
// pop up verified
$(document).ready(function () {
  $("#getStarted").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal").modal("show");
  });

  $("#waliForm").on("submit", function (event) {
    event.preventDefault();
    showModal();
  });

  $(".close").on("click", function () {
    $("#verificationModal").modal("hide");
  });
  $(".close-btn").on("click", function () {
    window.location.href = "login.html";
  });
});

// animasi pop up form login
$(document).ready(function () {
  $("#getLogin").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal2").modal("show");
  });

  $("#loginForm").on("submit", function (event) {
    event.preventDefault(); // Mencegah form dari pengiriman default
    showModal(); // Menampilkan modal
  });
  // Menutup modal hanya jika tombol OK diklik
  $(".close").on("click", function () {
    $("#verificationModal2").modal("hide");
  });
  $(".close-btn3").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
    window.location.href = "login.html"; // Pindah ke halaman homepage.html
  });
  $(".close-btn4").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman dashboard.html
    window.location.href = "signup.html"; // Pindah ke halaman dashboardwali.html
  });
});
// teks sembuyikan login
$(document).ready(function () {
  $("#toggleButton").click(function () {
    $("#infoText").toggle(); // Menyembunyikan atau menampilkan teks
    $(this).text(
      $(this).text() === "Sembunyikan Teks"
        ? "Tampilkan Teks"
        : "Sembunyikan Teks"
    ); // Mengubah teks tombol
  });
});
