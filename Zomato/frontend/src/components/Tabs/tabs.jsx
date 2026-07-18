import Icon, { DropboxOutlined, HeartOutlined, HomeOutlined } from '@ant-design/icons';
import { Tabs,Spin } from 'antd';
import { useState, Suspense, lazy } from 'react';
import Home from '../private-folder/homePage';
const LikedItems = lazy(() => import('../private-folder/likedItems'));
const MyOrders = lazy(() => import('../private-folder/myOrders'));



const FooterTab = () => {

  const [allFoodList, setAllFoodList] = useState([]);

  const items = [
    {
      key: '1',
      label: 'Liked Items',
      children: <Suspense
        fallback={<div style={{display:"flex",alignItems:"center", justifyContent:"center"}}><Spin spinning={true} size={"large"}></Spin></div>}>
        <LikedItems allFoodList={allFoodList} setAllFoodList={setAllFoodList} />
      </Suspense>,
      icon: <HeartOutlined />
    },
    {
      key: '2',
      label: 'Home',
      children: <Home allFoodList={allFoodList} setAllFoodList={setAllFoodList} />,
      icon: <HomeOutlined />
    },
    {
      key: '3',
      label: 'My Orders',
      children: <Suspense
        fallback={<div style={{display:"flex",alignItems:"center", justifyContent:"center"}}><Spin spinning={true} size={"large"}></Spin></div>}>
        <MyOrders />
      </Suspense>,
      icon: <DropboxOutlined />
    },
  ];
  return (
    <>
      <Tabs defaultActiveKey="2" items={items} centered size='large' tabBarGutter={50} />
    </>
  )
}

export default FooterTab;