export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  image:string;
  rating:number;
  link:string;
}

export const products = [
  {
    id: 1,
    name: 'Samsung Galaxy A23',
    price: 102834,
    description: 'A large phone with one of the best screens',
    image:'assets/images/phone1.jpg',
    rating:5,
    link:'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-chernyi-104348541/?c=750000000#!/item'
  },
  {
    id: 2,
    name: 'Samsung Galaxy A13',
    price: 89255,
    description: 'A great phone with one of the best cameras',
    image:'assets/images/phone2.jpg',
    rating:5,
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-128-gb-chernyi-104253279/?c=750000000#!/item'
  },
  {
    id: 3,
    name: 'Samsung Galaxy A33',
    price: 128398,
    description: 'A large phone with one of the best screens',
    image:'assets/images/phone3.jpg',
    rating:5,
    link:'https://kaspi.kz/shop/p/samsung-galaxy-a33-5g-6-gb-128-gb-chernyi-104398547/?c=750000000#!/item'
  }
];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/