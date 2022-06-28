var output = document.getElementById("demo");

var slider = document.getElementById("myRange").oninput = function () {

  var value = (this.value - this.min)

  output.innerHTML = value;
};
