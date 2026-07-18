import React, { useEffect, useMemo, useState } from 'react';
import { Card, Input, Select, Rate, Row, Col, Empty, Re, Result } from 'antd';
import './homePage.css';
import Icon, {
    HeartFilled,
    HeartOutlined,
    LikeFilled,
    LikeOutlined,
    ShoppingCartOutlined
} from '@ant-design/icons';
import HeartSvg from '../commonIcons/heartIcon';

const { Meta } = Card;
const { Search } = Input;
const { Option } = Select;


const LikedItems = ({allFoodList,setAllFoodList}) => {
    console.log("liked items")

    const [cartItems,setCartItems]=useState([])
    const [foodList, setFoodList] = useState([]);
    const [searchvalue, setSearchValue] = useState("")
    const HeartIcon = props => <Icon component={HeartSvg} {...props} />;

    const debounce = (fun, delay) => {
        let timer;
        return (value) => {
            clearTimeout(timer)
            timer = setTimeout(() => {
                fun(value)
            }, delay)
        }
    }

    const getSearchValue = (value, filter) => {
        let filteredValue;

        filteredValue = foodList.filter(data =>
            data.food_name?.toLowerCase().includes(value.toLowerCase()) ||
            data.restaurant_name?.toLowerCase().includes(value.toLowerCase())
        );
        setCartItems(filteredValue)
    }


    const getSearchFoodList = useMemo(() => {
        return debounce(getSearchValue, 300)
    }, [foodList])

    React.useEffect(() => {
        const items = (allFoodList || []).filter(item => item.isliked === true);
        setCartItems(items);
        setFoodList(items);
    }, [allFoodList]);

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

    return (
        <>
            <div className="home-container">
                <div className="controls">
                    {cartItems.length ? <Search
                        placeholder="Search food or Restaurant"
                        enterButton
                        allowClear
                        style={{ maxWidth: 480 }}
                        onChange={(e) => getSearchFoodList(e.target.value)} 
                    />:null}
                </div>
                <div className="cards">
                    {cartItems.length ?
                        <Row gutter={[16, 16]}>
                            { cartItems.map((food) => {
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
                                                -
                                                <span className="rating-text">{food.price} RS</span>

                                            </div>
                                            <div className="add-to-cart-sec">
                                                <div>
                                                    <div>
                                                        <b>Restaurant:</b> {food.restaurant_name}
                                                    </div>
                                                    <div>
                                                        <b>Address:</b> {food.hotel_address}
                                                    </div>
                                                </div>
                                                <div onClick={() => handleLikedProducts(food.id)}>
                                                    Remove from Liked Items <HeartIcon style={{ color: 'hotpink' }} />
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



                </div>
            </div>
        </>
    )
}

export default LikedItems;