import React, { useEffect, useState } from 'react';
import { Table, Button, Dropdown } from 'react-bootstrap';
import { observer } from 'mobx-react-lite';
import { fetchGoods } from "../http/productAPI";
import { PRODUCT_ROUTE } from '../utils/consts';

const TableProduct = observer(() => {
  const [products, setProducts] = useState([]);
  const [sortCriteria, setSortCriteria] = useState(null);
  const [sortDirection, setSortDirection] = useState(1);
  const [priceRange, setPriceRange] = useState('all');
  const [currentPage, setCurrentPage] = useState(1); // Состояние для хранения текущей страницы
  const [itemsPerPage] = useState(5); // Количество товаров на одной странице

  useEffect(() => {
    fetchGoods()
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  const sortProducts = (criteria) => {
    const sortedProducts = [...products].sort((a, b) => {
      if (a[criteria] < b[criteria]) return -sortDirection;
      if (a[criteria] > b[criteria]) return sortDirection;
      return 0;
    });
    setProducts(sortedProducts);
    setSortCriteria(criteria);
  };

  const handleSort = (criteria) => {
    if (criteria === sortCriteria) {
      setSortDirection(-sortDirection);
    } else {
      setSortCriteria(criteria);
      setSortDirection(1);
    }
    sortProducts(criteria);
  };

  const handleShowDetails = (id) => {
    //history.push(PRODUCT_ROUTE + '/' + id);
  };

  const filterByPriceRange = (product) => {
    if (priceRange === 'all') return true;
    const [min, max] = priceRange.split('-');
    return product.price >= parseFloat(min) && product.price <= parseFloat(max);
  };

  // Вычисление индекса первого и последнего элемента на текущей странице
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentProducts = products.filter(filterByPriceRange).slice(indexOfFirstItem, indexOfLastItem);

  // Функция для переключения на следующую страницу
  const nextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  // Функция для переключения на предыдущую страницу
  const prevPage = () => {
    setCurrentPage(currentPage - 1);
  };

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Товары</h1>
      <Dropdown>
        <Dropdown.Toggle variant="primary" id="dropdown-basic">
          Выберите диапазон цен
        </Dropdown.Toggle>

        <Dropdown.Menu>
          <Dropdown.Item onClick={() => setPriceRange('all')}>Все</Dropdown.Item>
          <Dropdown.Item onClick={() => setPriceRange('0-500')}>0 - 500</Dropdown.Item>
          <Dropdown.Item onClick={() => setPriceRange('501-1000')}>501 - 1000</Dropdown.Item>
          <Dropdown.Item onClick={() => setPriceRange('1001-10000000')}>1001 - </Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>

<Table striped bordered hover>
<thead>
  <tr>
    <th style={{ cursor: "pointer" }} onClick={() => handleSort('goods_id')}>
      ID {sortCriteria === 'goods_id' && sortDirection === 1 ? '▲' : '▼'}
    </th>
    <th style={{ cursor: "pointer" }} onClick={() => handleSort('goods')}>
      Name {sortCriteria === 'goods' && sortDirection === 1 ? '▲' : '▼'}
    </th>
    <th>Description</th>
    <th style={{ cursor: "pointer" }} onClick={() => handleSort('price')}>
      Price {sortCriteria === 'price' && sortDirection === 1 ? '▲' : '▼'}
    </th>
    <th style={{ cursor: "pointer" }} onClick={() => handleSort('amount')}>
      Amount {sortCriteria === 'amount' && sortDirection === 1 ? '▲' : '▼'}
    </th>
    <th></th>
  </tr>
</thead>
<tbody>
  {currentProducts.map(product => (
    <tr key={product.goods_id}>
      <td>{product.goods_id}</td>
      <td onClick={() => handleShowDetails(product.goods_id)}>{product.goods}</td>
      <td>{product.description}</td>
      <td>{product.price}</td>
      <td>
        {product.amount}
        {/*  */}
      </td>
      <td><Button variant={'outline-danger'}>В корзину</Button></td>
    </tr>
  ))}
</tbody>
</Table>
{/* Кнопки для переключения страниц */}
<div style={{ display: 'flex', justifyContent: 'center' }}>
<Button variant="secondary" onClick={prevPage} disabled={currentPage === 1}>
  Предыдущая страница
</Button>
<Button variant="secondary" onClick={nextPage} disabled={currentProducts.length < itemsPerPage}>
  Следующая страница
</Button>
</div>
</div>
);
});

export default TableProduct;
