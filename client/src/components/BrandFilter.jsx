import React, { useState, useEffect } from 'react';
import { Dropdown } from 'react-bootstrap';
import { fetchBrands } from '../http/productAPI';

const BrandFilter = ({ onSelectBrand }) => {
  const [brands, setBrands] = useState([]);

  useEffect(() => {
    fetchBrands()
      .then(data => setBrands(data))
      .catch(error => console.error('Error fetching brands:', error));
  }, []);

  return (
    <Dropdown>
      <Dropdown.Toggle variant="primary" id="dropdown-basic">
        Выберите бренд
      </Dropdown.Toggle>

      <Dropdown.Menu>
        {brands.map(brand => (
          <Dropdown.Item key={brand.brand_id} onClick={() => onSelectBrand(brand.brand)}>
            {brand.brand}
          </Dropdown.Item>
        ))}
      </Dropdown.Menu>
    </Dropdown>
  );
};

export default BrandFilter;