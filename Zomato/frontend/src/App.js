import logo from './logo.svg';
import './App.css';
import Login from './components/sign-up/Login';
import Signup from './components/sign-up/Signup';
import Home from './components/private-folder/homePage';
import PrivateRoute from "./components/privateRoute";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import FooterTab from './components/Tabs/tabs';
import BuyScreen from './components/private-folder/buyScreen';
import { OtpScreen } from './components/sign-up/OtpScreen';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />

        <Route path="/homepage" element={<PrivateRoute>
          <FooterTab />
        </PrivateRoute>} />
        <Route path="/buy" element={<PrivateRoute>
          <BuyScreen />
        </PrivateRoute>} />
         <Route path="/otp" element={<OtpScreen />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
