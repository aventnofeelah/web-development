import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';
import { PRODUCTS } from '../../data/products';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-list.html',
  styleUrls: ['./product-list.css']
})
export class ProductListComponent {
  products: Product[] = PRODUCTS;
  shareWhatsApp(link: string) {
    const encodedLink = encodeURIComponent(link);
    const url = `https://wa.me/?text=Посмотрите этот продукт: ${encodedLink}`;
    window.open(url, '_blank');
  }

  shareTelegram(link: string, name: string) {
    const encodedLink = encodeURIComponent(link);
    const encodedText = encodeURIComponent(name);

    const url = `https://t.me/share/url?url=${encodedLink}&text=${encodedText}`;
    window.open(url, '_blank');
  }
}
