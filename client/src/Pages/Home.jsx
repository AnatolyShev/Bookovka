import React, {useContext, useEffect} from 'react'
import { useNavigate} from 'react-router-dom'
import { Card, Col, Container, Row } from 'react-bootstrap'
// import styles from './Home.module.css'
// import Button from 'react-bootstrap/Button'
// import { SHOP_ROUTE } from '../utils/consts'
// import ProductList from '../components/ProductList'
import { observer } from 'mobx-react-lite'
// import { Context } from '../index'
import {fetchBrands, fetchProducts, fetchTypes, fetchCategory} from "../http/productAPI";
// import Pages from '../components/Pages'


const Home = observer(() => {
  const history = useNavigate();
  // const {user} = useContext(Context)
  // const {product} = useContext(Context)

  // useEffect(() => {
  //   fetchTypes().then(data => product.setTypes(data))
  //   fetchBrands().then(data => product.setBrands(data))
  //   fetchCategory().then(data => product.setCategories(data))
  //   fetchProducts(null, null, null, product.page, product.limit).then(data => {
  //       product.setProducts(data.rows)
  //       product.setTotalCount(data.count)
  //   })
  // }, [])

  // useEffect(() => {
  //   fetchProducts(product.selectedType.id, product.selectedBrand.id, product.selectedCategory.id, product.page, product.limit).then(data => {
  //       product.setProducts(data.rows)
  //       product.setTotalCount(data.count)
  //   })
  // }, [product.page, product.selectedType, product.selectedBrand, product.selectedCategory])

  return (
    <h1>Проект онлайн-магазина книг и канцелярских товаров</h1>
  )
})

export default Home