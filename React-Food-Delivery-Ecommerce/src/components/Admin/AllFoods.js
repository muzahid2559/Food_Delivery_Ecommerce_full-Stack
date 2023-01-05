import React, { useEffect, useState } from "react";
import { Button, Col, Table } from "reactstrap";
import axiosInstance from "../../utils/axiosInstance";

function AllOrder() {
  const [foods, setFoods] = useState();
  const fetchFoods = async () => {
    const response = await axiosInstance.get("").catch((e) => {
      console.log(e.response);
    });
    setFoods(response.data);
  };
  useEffect(() => {
    fetchFoods();
  }, []);
  return (
    <Col className="col-md-8">
      <span className="text-left mr-0">
        <Button>Create New Food</Button>
      </span>
      <h1 className="mb-3 text-center mt-10">
        <u>All Food</u>
      </h1>
      <Table borderless hover striped responsive>
        <thead>
          <tr>
            <th style={{ width: "1vw" }}>#</th>
            <th style={{ width: "10vw" }}>Image</th>
            <th>Title</th>
            <th>Price</th>
            <th style={{ width: "15.5vw" }}></th>
          </tr>
        </thead>
        <tbody>
          {foods?.map((item, id) => (
            <tr style={{ lineHeight: "15vh"}}>
              <td>{id}</td>
              <td>
                <div style={{ width: "75px", height: "75px", position: "absolute"}}><img style={{ width: "100%", height:"100%", position:"relative" }} alt="product_image" src={item.image} /></div>
              </td>
              <td>{item.title}</td>
              <td>৳{item.price}</td>
              <td>
                <Button>Hide</Button>
                &nbsp;
                <Button color="success">Edit</Button>
                &nbsp;
                <Button color="danger">Delete</Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Col>
  );
}

export default AllOrder;
