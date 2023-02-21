$(function () {
  const el = "<li>Item</li>";
  $("#add_item").bind("click", function () {
    $(".my_list").append(el);
  });
  $("#remove_item").bind("click", function () {
    $(".my_list li:last").remove();
  });
  $("#clear_list").bind("click", function () {
    $(".my_list").empty();
  });
});
