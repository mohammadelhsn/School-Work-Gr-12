class Person {
	constructor(first_name, last_name) {
		this.first_name = first_name;
		this.last_name = last_name;
		this.getFirstName = this.getFirstName;
		this.getLastName = this.getLastName;
	}
	getFirstName() {
		return this.first_name;
	}
	getLastName() {
		return this.last_name;
	}
}

const a = new Person();
console.log(a);
