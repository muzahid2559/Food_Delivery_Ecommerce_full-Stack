import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";

import AddCategory from "../components/Admin/AddCategory";
import Admin from "../components/Admin/Admin";
import CreateFood from "../components/Admin/CreateFood";
import UpdateCategory from "../components/Admin/UpdateCategory";
import Table from "../components/Deliver/Table";
import EditProfile from "../components/Profile/EditProfile";
import Profile from "../components/Profile/Profile";
import OrderTable from "../components/User/OrderTable";
import AllFoods from "../pages/AllFoods";
import Cart from "../pages/Cart";
import Checkout from "../pages/Checkout";
import FoodDetails from "../pages/FoodDetails";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Logout from "../pages/Logout";
import Register from "../pages/Register";
import RouteBuyer from "./BuyerRoute";
import RouteDeliver from "./RouteDeliver";
import RoutePrivate from "./RoutePrivate";
import RouteSeller from "./SellerRoute";

const Routers = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route path="/home" element={<Home />} />
      <Route path="/foods" element={<AllFoods />} />
      <Route path="/foods/:id" element={<FoodDetails />} />
      <Route path="/cart" element={<Cart />} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route element={<RoutePrivate />}>
        <Route path="/logout" element={<Logout />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/edit-profile" element={<EditProfile />} />
        <Route element={<RouteBuyer />}>
          <Route path="/order" element={<OrderTable />} />
          <Route path="/checkout" element={<Checkout />} />
        </Route>
        <Route element={<RouteSeller />}>
          <Route path="/food/category/create" element={<AddCategory />} />
          <Route
            path="/food/category/update/:id"
            element={<UpdateCategory />}
          />
          <Route path="/food/create" element={<CreateFood />} />
          <Route path="/seller" element={<Admin />} />
          <Route path="/all-foods" element={<Admin />} />
        </Route>
        <Route element={<RouteDeliver />}>
          <Route path="/deliver-table" element={<Table />} />
        </Route>
      </Route>
    </Routes>
  );
};

export default Routers;
