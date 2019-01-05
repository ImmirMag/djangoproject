function addcookie(id,name,value){
    document.cookie = (id + name + '=' + value)

}


function deletepost(post){
var p = String(post)
var parent = document.getElementById('posts');
var elem = document.getElementById(p);
parent.removeChild(elem);
}

