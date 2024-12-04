var input = document.getElementById("SearchInput");

input.onkeyup = function () {
    var filter = input.value.toLowerCase();
    var lis = document.getElementById("DataContainer").getElementsByTagName("ul")[0].getElementsByTagName("li");

    // TODO: this can be replaced with actual fuzzy search e.g. string distance and sorting instaed
    for (var i = 0; i < lis.length; i++) {
        var data = lis[i].innerText;
        if (data.toLowerCase().indexOf(filter) == 0) {
            lis[i].style.display = "block";
        }
        else {
            lis[i].style.display = "none";
        }
    }
}