package eapi

import (
    "bytes"
    "encoding/json"
    "net/http"
    "crypto/tls"
)

type Client struct {
    Addr     string
    Username string
    Password string
}

func New(addr, user, pass string) *Client {
    return &Client{
        Addr:     addr,
        Username: user,
        Password: pass,
    }
}

func (c *Client) RunCmds(cmds []string) ([]json.RawMessage, error) {
    payload := map[string]interface{}{
        "jsonrpc": "2.0",
        "method":  "runCmds",
        "params": map[string]interface{}{
            "version": 1,
            "cmds":    cmds,
        },
        "id": 1,
    }

    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest(
        "POST",
        "https://"+c.Addr+"/command-api",
        bytes.NewBuffer(body),
    )
    req.SetBasicAuth(c.Username, c.Password)
    req.Header.Set("Content-Type", "application/json")
    tr := &http.Transport{
	    TLSClientConfig: &tls.Config{
		    InsecureSkipVerify: true,
	    },
    }
    client := &http.Client{
	    Transport: tr,
    }

    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    var result struct {
        Result []json.RawMessage `json:"result"`
    }

    err = json.NewDecoder(resp.Body).Decode(&result)
    return result.Result, err
}
