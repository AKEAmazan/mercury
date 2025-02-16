import { v4 as uuidv4 } from 'uuid';
import axios from "axios";

export const getSessionId = () => {
    var sessionId = sessionStorage.getItem("sessionId");
    if (sessionId == null) {
        sessionId = uuidv4();
        sessionStorage.setItem("sessionId", sessionId);
    }
    return sessionId;
}

export const setAxiosAuthToken = (token: string | null) => {
    if (typeof token !== "undefined" && token) {
        // Apply for every request
        axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
        // Delete auth header
        delete axios.defaults.headers.common["Authorization"];
    }
};