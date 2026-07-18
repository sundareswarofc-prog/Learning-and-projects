import React, { Children, useEffect, useMemo, useState } from 'react';
import { Card, Input, Select, Rate, Row, Col, Empty, Re, Result, Button, FloatButton, Modal, Spin, Tabs } from 'antd';
import './homePage.css';
import Icon, {
    FilterOutlined,
    HeartFilled,
    HeartOutlined,
    HeartTwoTone,
    LikeFilled,
    LikeOutlined,
    ShoppingCartOutlined
} from '@ant-design/icons';
import HeartSvg from '../commonIcons/heartIcon';
import { useNavigate } from 'react-router-dom';
import useFetchApiHook from '../../customHook/getApIHook';

const { Meta } = Card;
const { Search } = Input;
const { Option } = Select;

const Home = ({ allFoodList, setAllFoodList }) => {
    const navigate = useNavigate()
    const [foodList, setFoodList] = useState([]);
    const [searchvalue, setSearchValue] = useState("")
    const { data, loading, error } = useFetchApiHook("http://localhost:5000/foodlist")
    const [modalOpen, setModalOpen] = useState({
        isCartModalOpen: false,
        isFilterModalOpen: false,
        isPageLoding: true
    });
    const [defaultValue, setDefaultValue] = useState({
        rating: 0,
        categories: 0,
        price: 0
    })
    const ratings = [...new Set(foodList.map(item => item.restaurant_rating))];
    const categories = [...new Set(foodList.map(item => item.category_name))]
    const priceFilterArray = [...new Set(foodList.map(item => item.price))].sort((a, b) => Number(a) - Number(b));
    const HeartIcon = props => <Icon component={HeartSvg} {...props} />;
    const cartCount = allFoodList.filter(item => item.iscart);
    const PriceTotal = cartCount.reduce(
        (acc, item) => acc + Number(item.price),
        0
    );
    const priceOptions = [];

    for (let i = 0; i <= priceFilterArray[priceFilterArray.length - 1]; i += 100) {
        priceOptions.push(i);
    }
    const [filters, setFilters] = useState({
        rating: 0,
        categories: "",
        price: "0"
    });

    useEffect(() => {
        if (data.length) {
            setAllFoodList(data)
            setFoodList(data)
            setModalOpen(prev => ({ ...prev, isPageLoding: loading }))
        }
        else {
            console.log(error)
        }
    }, [data, loading, error])


    const debounce = (fun, delay) => {
        let timer;
        return (value) => {
            clearTimeout(timer)
            timer = setTimeout(() => {
                fun(value)
            }, delay)
        }
    }

    const getSearchValue = (value) => {
        let filteredValue;
        filteredValue = foodList.filter(data =>
            data.food_name?.toLowerCase().includes(value.toLowerCase()) ||
            data.restaurant_name?.toLowerCase().includes(value.toLowerCase())
        );
        setAllFoodList(filteredValue)
    }

    const getFilterData = (value, filter) => {
        setFilters(prev => ({
            ...prev,
            [filter]: value
        }));
        setDefaultValue(prev => (
            {
                ...prev,
                [filter]: value
            }
        )
        )
    }

    const applyFilter = () => {
        let filtered = [...foodList];

        if (filters.rating !== 0) {
            filtered = filtered.filter(
                item => item.restaurant_rating === filters.rating
            );
        }
        if (filters.categories) {
            filtered = filtered.filter(
                item => item.category_name === filters.categories
            );
        }

        if (filters.price !== '0') {
            const [min, max] = filters.price.split("-");

            if (max === "max") {
                filtered = filtered.filter(
                    item => Number(item.price) >= Number(min)
                );
            } else {
                filtered = filtered.filter(
                    item =>
                        Number(item.price) >= Number(min) &&
                        Number(item.price) < Number(max)
                );
            }
        }
        if (filtered)
            setAllFoodList(filtered);
        setModalOpen(prev => ({ ...prev, isFilterModalOpen: false }));
        setFilters({
            rating: 0,
            category: "",
            price: "0"
        })
    }

    const getSearchFoodList = useMemo(() => {
        return debounce(getSearchValue, 300)
    }, [foodList])

    const handleLikedProducts = async (id) => {
        const previous = allFoodList;
        setAllFoodList(prev =>
            prev.map(item =>
                item.id === id ? { ...item, isliked: !item.isliked } : item
            )
        );

        try {
            const result = await fetch('http://localhost:5000/likeditems', {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id })
            })

            if (!result.ok) {
                setAllFoodList(previous);
            }
        } catch (err) {
            console.log(err);
            setAllFoodList(previous);
        }
    }

    const handleCartItems = async (id) => {
        setAllFoodList(prev =>
            prev.map(item =>
                item.id === id ? { ...item, iscart: !item.iscart } : item
            )
        );
        try {
            const result = await fetch('http://localhost:5000/cartedItems', {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id })
            })

        } catch (err) {
            console.log(err);
        }
    }

    const clearAll = () => {
        setAllFoodList(data);
        setModalOpen(prev => ({ ...prev, isFilterModalOpen: false }));
        setDefaultValue({
            rating: 0,
            categories: 0,
            price: 0
        })
    }

    return (
        <div className="home-container">
            <div className="controls">
                <Search
                    placeholder="Search food or Restaurant"
                    enterButton
                    allowClear
                    style={{ maxWidth: 480 }}
                    onChange={(e) => getSearchFoodList(e.target.value)}
                />

                <div><Button onClick={() => setModalOpen(prev => ({ ...prev, isFilterModalOpen: true }))}><FilterOutlined /> Filters</Button></div>

                <Button type='danger' onClick={()=>{localStorage.removeItem('token');navigate("/")}}>Log Out</Button>

            </div>
            <Modal
                open={modalOpen.isFilterModalOpen}
                onCancel={() => setModalOpen(prev => ({
                    ...prev,
                    isFilterModalOpen: false
                }))}
                footer={(_, { CancelBtn }) => (
                    <>
                        <Button type='primary' onClick={applyFilter}>Apply</Button>
                        <Button type='' disabled={(filters.rating == 0) && (filters.categories == "") && (filters.price == "0")} onClick={clearAll}>Clear All</Button>
                    </>
                )}>

                <div style={{ display: "flex", justifyContent: "center", gap: "15px", marginBottom:"21px" }}>
                    <div className="">
                        <Select value={defaultValue.rating} onChange={(value) => getFilterData(value, "rating")} style={{ minWidth: 100 }}>
                            <Option value={0}>All ratings</Option>
                            {ratings.map((data, i) => {
                                return (
                                    <Option value={data} key={i}>{data}</Option>
                                )
                            })
                            }
                        </Select>
                    </div>
                    <div className="">
                        <Select value={defaultValue.categories} onChange={(value) => getFilterData(value, "categories")} style={{ minWidth: 100 }}>
                            <Option value={0}>All categories</Option>
                            {categories.map((data, i) => {
                                return (
                                    <Option value={data} key={i}>{data}</Option>
                                )
                            })
                            }
                        </Select>
                    </div>
                    <div className="">
                        <Select value={defaultValue.price} onChange={(value) => getFilterData(value, "price")} style={{ minWidth: 100 }}>
                            <Option value={0}>Sort by price (₹)</Option>
                            {priceOptions.map((data, i) => {
                                return (
                                    <Option value={`${data}-${priceOptions[i + 1] || "max"}`} key={i}> {priceOptions[i + 1]
                                        ? `₹${data} - ₹${priceOptions[i + 1]}`
                                        : `Above ₹${data}`}</Option>
                                )
                            })
                            }
                        </Select>
                    </div>
                </div>

            </Modal>

            <div className="cards">
                <Spin spinning={modalOpen.isPageLoding} size={"large"}>
                    {allFoodList.length ?
                        <div>
                            <Row gutter={[16, 16]}>
                                {allFoodList.length && allFoodList.map((food) => {
                                    return (
                                        <Col xs={24} sm={12} md={8} lg={6} key={food.id}>
                                            <Card className="food-card" hoverable>
                                                <div className="food-card-top">
                                                    <div className="food-img" />
                                                    <Meta title={food.food_name} description={food.description} />
                                                </div>
                                                <div className="food-card-footer">
                                                    <Rate allowHalf disabled defaultValue={food.restaurant_rating} />
                                                    <span className="rating-text">{food.restaurant_rating}</span>
                                                </div>
                                                <div className="like-sec">
                                                    <div>
                                                        <div>
                                                            <b>Restaurant:</b> {food.restaurant_name}
                                                        </div>
                                                        <div>
                                                            <b>Address:</b> {food.hotel_address}
                                                        </div>
                                                    </div>
                                                    <div>
                                                        <div onClick={() => handleLikedProducts(food.id)} style={{ marginBottom: "10px" }}>
                                                            Add to Liked Items {food.isliked ? <HeartIcon style={{ color: 'hotpink' }} /> : <HeartOutlined />}
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className='add-to-cart-sec'>
                                                    <div>
                                                        <Button type="primary" onClick={() => handleCartItems(food.id)}>{food.iscart ? "Remove from Cart" : "Add to Cart"}<ShoppingCartOutlined /></Button>
                                                    </div>
                                                    <div>
                                                        <Button onClick={() => navigate("/buy")}>
                                                            <b>Buy / ₹{food.price}</b>
                                                        </Button>
                                                    </div>


                                                </div>
                                            </Card>
                                        </Col>
                                    )
                                })
                                }
                            </Row>


                        </div> : null
                    }
                </Spin>
                {allFoodList.length === 0 ?
                    <Result
                        status="warning"
                        title="No items found"
                    /> : null
                }

            </div>
            {cartCount.length > 0 &&
                <FloatButton
                    shape="square"
                    type="primary"
                    style={{ insetInlineEnd: 94 }}
                    icon={<ShoppingCartOutlined />}
                    badge={{ count: cartCount.length, color: 'red' }}
                    onClick={() => setModalOpen(prev => ({
                        ...prev,
                        isCartModalOpen: true
                    }))}
                />
            }
            <Modal
                open={modalOpen.isCartModalOpen}
                title="Cart List"
                onCancel={() => setModalOpen(prev => ({
                    ...prev,
                    isCartModalOpen: false
                }))}
                styles={{
                    body: {
                        overflowX: "hidden",
                        maxHeight: "600px",
                        overflowY: "auto"
                    }
                }}
                footer={(_, { OkBtn, CancelBtn }) => (
                    <>
                        {cartCount.length ? <>

                            <Button type='primary'>Buy all @ ₹{PriceTotal && PriceTotal}</Button>
                            <CancelBtn /></>
                            : null}
                    </>
                )}
            >
                {cartCount.length ?
                    <Row gutter={[16, 16]} >
                        {cartCount.length && cartCount.map((food) => {
                            return (
                                <Col span={24} key={food.id}>
                                    <Card className="" hoverable>
                                        <div className="food-card-top">
                                            <div className="food-img" />
                                            <Meta title={food.food_name} description={food.description} />
                                        </div>
                                        <div className="food-card-footer">
                                            <Rate allowHalf disabled defaultValue={food.restaurant_rating} />
                                            <span className="rating-text">{food.restaurant_rating}</span>
                                            -
                                            <span className="rating-text">{food.price} RS</span>

                                        </div>
                                        <div className="like-sec">
                                            <div>
                                                <div>
                                                    <b>Restaurant:</b> {food.restaurant_name}
                                                </div>
                                                <div>
                                                    <b>Address:</b> {food.hotel_address}
                                                </div>
                                            </div>
                                            <div>
                                                <div onClick={() => handleLikedProducts(food.id)} style={{ marginBottom: "10px" }}>
                                                    Add to Liked Items {food.isliked ? <HeartIcon style={{ color: 'hotpink' }} /> : <HeartOutlined />}
                                                </div>
                                            </div>
                                        </div>
                                        <div className='add-to-cart-sec'>
                                            <div>
                                                <Button type="primary" onClick={() => handleCartItems(food.id)}>{food.iscart ? "Remove from Cart" : "Add to Cart"}<ShoppingCartOutlined /></Button>
                                            </div>
                                            <div>
                                                <Button >
                                                    <b>Buy / ₹{food.price}</b>
                                                </Button>
                                            </div>


                                        </div>
                                    </Card>
                                </Col>
                            )
                        })
                        }
                    </Row> :
                    <div>
                        <Result
                            status="warning"
                            title="No items found"
                        />
                    </div>
                }
            </Modal>
        </div>

    );
};

export default Home;