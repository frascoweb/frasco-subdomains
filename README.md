# Frasco-Subdomains

Extract the subdomain variable from the request values

## Installation

    pip install frasco-subdomains

## Setup

Feature name: subdomains

Options:

 - *param_name*: the name of the URL parameter

## Usage

This feature will simply remove the parameter from the URL values before the request
is dispatched and insert it again when building urls.

The value of the parameter is available using the `$subdomain` variable in the context.

To declare a subdomain for a blueprint, in its *__init__.yml* add:

    subdomain: <subdomain>