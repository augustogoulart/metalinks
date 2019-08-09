import axios from 'axios'


const serviceApi = axios.create({
  baseURL: process.env.SERVICE_URL || "http://localhost:8000/",
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  parseMetaData(link) {
    return serviceApi.post('services/parser/', link)
  }
}
