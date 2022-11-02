function random(a,b){
    return a + Math.random()*(b-a);
}

function getDistance(a,b){
    var dx=a.x-b.x;
    var dy=a.y-b.y;
    return Math.sqrt(dx*dx + dy*dy);
}

function getRandomColor(){
    var r=Math.floor(random(0,255));
    var g=Math.floor(random(0,255));
    var b=Math.floor(random(0,255));
    return 'rgb(' + r + ',' + g + ',' + b + ')' ;
}
function Ant(indx){ 
    this.radius=30;
    this.velocity=new Point();
    this.velocity.setDirection(random(0,2*Math.PI));
    this.velocity=this.velocity.scale(random(1,6));
    this.color=getRandomColor();    
    this.pos=new Point(random(this.radius,window.WIDTH-this.radius), random(this.radius,window.HEIGHT-this.radius));
    this.index=indx;
    this.collisionUpdate=function(balls)
    {
        //Vertical Collision
        if(this.pos.y>window.HEIGHT-this.radius || this.pos.y<this.radius)
        {
            this.velocity.y*=-1;
            if(this.pos.y<this.radius){
                this.pos.y=this.radius+1;}
            else{
                this.pos.y=window.HEIGHT-this.radius;
            }
        }
        //Horizontal Collision
        if(this.pos.x>window.WIDTH-this.radius || this.pos.x<this.radius)
        {
            this.velocity.x*=-1;
            if(this.pos.x < this.radius){
                this.pos.x= this.radius+1;}
            else{
               this.pos.x= window.WIDTH-this.radius;
            }
        }
        //Ball Collision
        for(var i=this.index+1;i<balls.length;i++){
            var ball=balls[i];
            var dist=getDistance(this.pos,ball.pos);
            var minimumDist=(this.radius+ball.radius)
            if(dist<=minimumDist){
                var temp=this.velocity;
                this.velocity=ball.velocity;
                ball.velocity=temp;
            }
        }
        
        this.pos.add(this.velocity);
    }
    
}