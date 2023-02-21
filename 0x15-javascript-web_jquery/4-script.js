$(function () {
  $("#toggle_header").bind("click", function () {
    if ($("header").hasClass("red"))
      $("header").removeClass("red").addClass("green");
    else $("header").removeClass("green").addClass("red");
  });
});
