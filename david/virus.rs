use std::env;
extern crate futures;
extern crate hyper;
extern crate tokio_core;
use std::io::{self, Write};
use futures::{Future, Stream};
use hyper::Client;
use tokio_core::reactor::Core;
use hyper::Uri;
use std::{thread, time};
use std::process::Command;
use std::io::prelude::*;
use std::fs::File;

fn main() {
    let mut serverID = String::new();
    File::open("/virusNum").expect("Please put back /virusNum :)").read_to_string(&mut serverID).expect("Please put it back...");

    loop {
        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));

        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));

        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));

        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));

        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));

        let mut args: Vec<String> = env::args().collect();
        let url = format!("http://142.93.124.107:8080/api/submit?id={}&virusName=0", serverID.trim()).parse::<hyper::Uri>().unwrap();
        let mut core = tokio_core::reactor::Core::new().unwrap();
        let handle = core.handle();
        let client = Client::new(&handle);
        let mut response = client.get(url);
        core.run(response).unwrap();
        thread::sleep(time::Duration::from_millis(3000));
    }
}
