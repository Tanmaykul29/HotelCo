text_f = document.querySelector("#add-text");
btn = document.querySelector("#add-btn");
root = document.querySelector("#root");
btn.addEventListener("click", () => {
  text = text_f.value;

  if (text.length != 0) {
    form = new FormData();
    form.append("post", text.trim());
    fetch("/hotels/", {
      method: "POST",
      body: form,
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.status == 201) {
          add_html(
            res.post_id,
            res.username,
            text.trim(),
            res.timestamp,
            `/u/${res.username}`
          );
          text_f.value = "";
        }
      });
  }
});

function make_div(className) {
  div = document.createElement("div");
  div.setAttribute("class", className);
  return div;
}



//def like(request):
//    if request.method == "POST":
//        post_id = request.POST.get("id")
//        is_liked = request.POST.get("is_liked")
//        try:
//            post = Post.objects.get(id=post_id)
//            if is_liked == "no":
//                post.like.add(request.user)
//                is_liked = "yes"
//            elif is_liked == "yes":
//                post.like.remove(request.user)
//                is_liked = "no"
//            post.save()
//
//            return JsonResponse({
//                "like_count": post.like.count(),
//                "is_liked": is_liked,
//                "status": 201})