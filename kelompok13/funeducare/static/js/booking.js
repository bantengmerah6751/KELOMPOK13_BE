// jQuery untuk menangani event klik tombol Cancel
$("#cancelButton").on("click", function () {
  window.location.href = "index.html";
});

// jQuery untuk menangani pengiriman form
$("#bookingForm").on("submit", function (event) {
  event.preventDefault();
  const parentName = $("#parentName").val();
  const email = $("#exampleInputEmail1").val();
  const phone = $("#phone").val();
  if (!parentName || !email || !phone) {
    alert("Mohon isi semua field yang diperlukan!");
    return;
  }
  // Simulasi pengiriman data
  alert("Booking berhasil untuk " + parentName);
  $(this).trigger("reset"); // Reset form setelah berhasil
});
