import axios from "axios";

/**
 * 登录
 * @param {*} body 
 * @returns 
 */
export async function login(body) {
  return axios.post("/account/login", body);
}
