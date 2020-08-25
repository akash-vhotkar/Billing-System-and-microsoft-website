const company = [
    { name: "company one", category: "finance", start: 1981, end: 2003 },
    { name: "company two", category: "retail", start: 1992, end: 2008 },
    { name: "company three", category: "auto", start: 1999, end: 2007 },
    { name: "company four", category: "retail", start: 1989, end: 2010 },
    { name: "company five", category: "tech", start: 2009, end: 2014 },
    { name: "company six", category: "finacial", start: 1987, end: 2010 },
    { name: "company seven", category: "auto", start: 1986, end: 1996 },
    { name: "company eight", category: "tech", start: 2011, end: 2016 },
    { name: "company nine", category: "retail", start: 1981, end: 1986 }

];
const ages = [22, 45, 665, 67, 44, 1, 23, 434, 34];
// for (let i = 0; i < ages.length; i++) {
//     console.log(ages[i]);
// }
// company.forEach(function (com) {
//     console.log(com.name);
// });
// // let candrink = [];
// const candrink = ages.filter(age => age >= 21);
// console.log(candrink); 

// const retail_company = company.filter(com => com.category == "retail");
// console.log(retail_company);
// 

// // const past_10 = company.filter(com => com.start > 1900 && com.end < 2000);
// // console.log(past_10);
// const company_name = company.map(function (com) {
//     return `${"comapany name is "}${com.name}`;
// // });
// // console.log(company_name);
// const ages_sq = ages.map(age => Math.sqrt(age));
// // const mul = ages.map(age => age * 2).map(age => Math.sqrt(age));
// // console.log(mul);
// // console.log(ages_sq);

// const soarted = company.sort((a, b) => b - a);
// // console.log(soarted);
// const heading = document.querySelector('h1');
// // const text = heading.innerHTML;
// // console.log(text);
// const list = document.querySelector('ul');
const btn = document.querySelector('.htmlbtn');
btn.addEventListener('click', (e) => {
    console.log(e.target.className)
});
const list = document.querySelector('ul');
console.log(list.children[0].className);