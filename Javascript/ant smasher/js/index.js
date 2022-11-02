var playarea=document.getElementById("playarea")
var ctx = playarea.getContext("2d");
var ants=[];
var antCount=10 ;
var offset=100;
var img=new Image();
img.src="css/ant.png";
var antArea=70

function resize(){
    window.WIDTH=window.innerWidth;
    window.HEIGHT=window.innerHeight;
    ctx.canvas.width=window.WIDTH;
    ctx.canvas.height=window.HEIGHT;
}
function update(){
    ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);
    ants.forEach(function (ant){
        ant.collisionUpdate(ants);
        ctx.save();
        ctx.translate(ant.pos.x,ant.pos.y);
        ctx.drawImage( img,0,0);
       ctx.restore();
    })
    requestAnimationFrame(update)
}

resize();

for(var i=0; i<antCount; i++){
    ants.push(new Ant(i));
}

function removeAnt(event){
    var x = event.clientX;
    var y = event.clientY;
    console.log(x,y)
    ants.forEach(function (ant,indx){
        if(getDistance(new Point(x,y),ant.pos) < antArea)
        {
            ants.splice(indx,1);
            for (var i=indx;i<ants.length;i++){
                ants[i].index=i-1
            }
            

        }
    })
}

playarea.addEventListener("click",removeAnt);
window.addEventListener("resize",resize)
requestAnimationFrame(update);
