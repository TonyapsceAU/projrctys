function setup() {
  createCanvas(windowWidth, windowHeight);
	colorMode(HSB);
	
	let values = [];
  let amount = width;
  for (let i=0;i<amount;i++) {
    values[i] = round(random(height));
  }
	
	let sortmode = 5;
	sortf = new Sort_animeted(sortmode,values);
}

function draw() {
  background(0);
	sortf.run();
  draw_rect(sortf.arr);
}



class Sort_animeted{
	constructor(mode,arr){
		this.proces_counter = 0;//take how long to sort
		this.cycle_count = 0;
		this.state = 0;//fincished:1 inprogress:0
		this.mode = mode;
		this.arr = arr;
		this.amount = arr.length;
		if(mode==3){
			this.big_c = this.biggest();
			this.dig = 1;
			this.amount_count = 0;
		}
		if(mode==5){
			this.end = this.amount-1;
			this.start = 0;
		}
	}
	
	run(){
		if (this.state) {
			print('finished',this.proces_counter);
			noLoop();
		} else {
			switch (this.mode) {
				case 0:
					this.bubble_sort(this.arr);
					break;
				case 1:
					this.selection_sort(this.arr);
					break;
				case 2:
					this.insertion_sort(this.arr);
					break;
				case 3:
					this.radix_sort(this.arr);
					if(this.amount_count>=this.amount){
						this.dig++;
						this.amount_count = 0;
					}else{
						this.amount_count++;
					}
					break;
				case 4:
					this.bogo_sort();
					break;
				case 5:
					this.idk_sort();
					break;
					
			}
			this.check_state();
		}
	}
	
	check_state(){
		switch (this.mode) {
				case 0:
				case 1:
				case 2:
					if(sortf.cycle_count<this.amount){
						this.state = 0;
					}else{
						this.state = 1;
					}
					break;
				case 3:
					if(this.dig>this.big_c){
						this.state = 1;
					}else{
						this.state = 0;
					}
					break;
				case 4:
					if(this.cycle_count>=100000){
						print("i give up");
						this.state = 1;
					}
					let n = 0;
					for(n=0;n<this.amount;n++){
						if(this.arr[n]>this.arr[n+1]){
							break;
						}
					}
					if(n==this.amount){
						this.state = 1;
					}else{
						this.state = 0;
					}
					break;
				case 5:
					if(this.end<this.start){
						this.state = 1;
					}
					break;
			}
	}
	//mode = 0
	bubble_sort(){
		for (let j=0;j<this.arr.length-this.cycle_count-1;j++) {
			if (this.arr[j] > this.arr[j + 1]) {
				[this.arr[j + 1],this.arr[j]] = [this.arr[j],this.arr[j + 1]];
			}
			this.proces_counter++;
		}
		this.cycle_count++;
	}
	//mode = 1
	selection_sort(){
		let min_v = this.cycle_count;
		for(let i=this.cycle_count;i<this.amount;i++){
			if(this.arr[i]<this.arr[min_v]){
				min_v = i;
			}
			this.proces_counter++;
		}
		[this.arr[min_v],this.arr[this.cycle_count]] = [this.arr[this.cycle_count],this.arr[min_v]];
		this.cycle_count++;
	}
	//mode = 2
	insertion_sort(){
		for(let i=0;i<this.cycle_count;i++){
			if(this.arr[this.cycle_count]<this.arr[i]){
				for(let j=i;j<this.cycle_count;j++){
					[this.arr[this.cycle_count],this.arr[j]] = [this.arr[j],this.arr[this.cycle_count]];
					this.proces_counter++;
				}
				break;
			}
		}
		this.cycle_count++;
	}
	//mode = 3
	radix_sort(){//n:proces_counter
		for(let i=0;i<this.amount-1;i++){
			let num1 = this.get_dig(this.arr[i],this.dig);
			let num2 = this.get_dig(this.arr[i+1],this.dig);
			if(num1>num2){
				[this.arr[i],this.arr[i+1]] = [this.arr[i+1],this.arr[i]];
			}
			this.proces_counter++;
		}
		this.cycle_count++;
	}
	
	get_dig(num,dig){
		let ans = floor(round(num/pow(10,dig)-floor(num/pow(10,dig)),dig)*10,0);
		return ans;
	}

	biggest(){
		let max_n = 0;
		for(let i=0;i<this.amount;i++){
			if(max_n<this.arr[i]){
				max_n = this.arr[i]
			}
		}
		let c=0;
		while(max_n>0){
			max_n = floor(max_n/10);
			c++;
		}
		return c;
	}
	//mode = 4
	bogo_sort(){
		let num = this.amount-1;
		let loop_am = round(random(1,num));
		for(let i=0;i<loop_am;i++){
			let num1 = round(random(0,num));
			let num2 = round(random(0,num));
			[this.arr[num1],this.arr[num2]] = [this.arr[num2],this.arr[num1]]
			this.proces_counter++;
		}
		this.cycle_count++;
	}
	//mode = 5
	idk_sort(){
		let max_value_index = this.end;
		let min_value_index = this.start;

		for(let i=this.start;i<this.end+1;i++){
			if(this.arr[i]>this.arr[max_value_index]){
				max_value_index = i;
			}
			this.proces_counter++
		}
		[this.arr[this.end],this.arr[max_value_index]] = [this.arr[max_value_index],this.arr[this.end]];

		for(let i=this.start;i<this.end+1;i++){
			if(this.arr[i]<this.arr[min_value_index]){
				min_value_index = i;
			}
			this.proces_counter++
		}
		[this.arr[this.start],this.arr[min_value_index]] = [this.arr[min_value_index],this.arr[this.start]];

		this.end--;
		this.start++;
	}
}

function draw_rect(values){
	let amount = values.length;
	for(i=0;i<amount;i++){
		x = i*(width/amount);
		hu = map(i,0,amount,0,360);
		fill(hu,100,100);
		stroke(hu,100,100);
		rect(x,height,(width/amount),-values[i]);
	}
}





