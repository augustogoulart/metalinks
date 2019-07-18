import axios from 'axios'


const apiClient = axios.create({
  // baseURL: process.env.BASE_URL || "http://localhost:8000/api/",
  baseURL: "https://involved-api.herokuapp.com/api/",
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  getLinks() {
    return apiClient.get('links/')
  },
  postLink(link) {
    return apiClient.post('links/', link)
  }
}
