function Point(x=1,y=1){
    this.x=x;
    this.y=y;

    this.unitVector=function(){
        var magnitude=this.getMagnitude();
        this.x = this.x / magnitude;
        this.y = this.y / magnitude;
        console.log(this.x,this.y)
    }

    this.setDirection=function(angle){
        var magnitude=this.getMagnitude();
        this.x=magnitude*Math.cos(angle);
        this.y=magnitude*Math.sin(angle);
    }

    this.getMagnitude=function(){
        return Math.sqrt(this.x*this.x + this.y*this.y);
    }

    this.add = function(point)
    {
        this.x += point.x;
        this.y += point.y;
    }

    this.scale=function(scaler){
        var n=new Point();
        n.x=this.x*scaler;
        n.y=this.y*scaler;
        return n;
    }

}