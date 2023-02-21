$(function () {
  $.ajax({
    type: "GET",
    url: "https://fourtonfish.com/hellosalut/?lang=fr?callback=?",
    dataType: "json",
    success: function (data) {
      $("#hello").text(data.hello);
    },
  });
});
