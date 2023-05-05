function setup() {
	createCanvas(windowWidth, windowHeight);
	
	start_ang = 70;
	amount = 9;
	pendulums = [];
	for(i=0;i<amount;i++){
		let temp = new Pendulum(50,550+25*i,start_ang,0,1,0,1);
		append(pendulums,temp);
	}
}

function draw() {
	background(0);
  translate(width/2,0);
	
	for(i=0;i<amount;i++){
		pendulums[i].run();
	}
}

class Pendulum{
  constructor( mass_, leng_ , ang_, angV_, angA_, force_, gravity_){    
		this.mass = mass_;
		this.leng = leng_;
		this.ang = ang_;
		this.angV =  angV_;
		this.angA =  angA_;
		this.force = force_;
		this.gravity = gravity_ ;
  }
	
	run() {
		this.angle = this.ang;

		this.force = this.gravity * sin(this.angle);
		this.angA = (-1*this.force)/this.leng;

		this.angV += this.angA;
		this.ang += this.angV;

		this.angV *= 0.999;

		this.x = this.leng * sin(this.angle);
		this.y = this.leng * cos(this.angle);



		strokeWeight(5);
		stroke(255);
		fill(255);
		line(0,0,this.x,this.y);
		ellipse(this.x,this.y,this.mass , this.mass);
		fill(100);
		ellipse(this.x,this.y,this.mass*0.95,this.mass*0.95);

		}
}
