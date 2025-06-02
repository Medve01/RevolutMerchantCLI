# Revolut Merchant API CLI

A command-line interface tool for managing Revolut Merchant API operations, including webhook management and order processing.

## Features

- **Webhook Management**
  - List registered webhooks
  - Register new webhooks
  - Delete existing webhooks
  - Purge all webhooks

- **Order Management**
  - Create new orders
  - List orders from a specified time window
  - Get detailed order information

## Prerequisites

- Bash shell
- `curl` for making HTTP requests
- `jq` for JSON formatting (optional but recommended)
- `pygmentize` for syntax highlighting (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Medve01/RevolutMerchantCLI.git
   cd RevolutMerchantCLI
   ```

2. Make the script executable:
   ```bash
   chmod +x revcli
   ```

3. Create your API key files:
   - For production: Create `revolut.secret.key` with your production API key
   - For sandbox: Create `revolut.sandbox.secret.key` with your sandbox API key

## Usage

### Basic Syntax

```bash
./revcli <command> [options]
```

### Commands

#### Webhook Management

1. List all webhooks:
   ```bash
   ./revcli webhook list [-e sandbox|production]
   ```

2. Register a new webhook:
   ```bash
   ./revcli webhook register <url> [-e sandbox|production]
   ```

3. Delete a webhook:
   ```bash
   ./revcli webhook delete <id> [-e sandbox|production]
   ```

4. Delete all webhooks:
   ```bash
   ./revcli webhook purge [-e sandbox|production]
   ```

#### Order Management

1. Create a new order:
   ```bash
   ./revcli order create <amount> <currency> [-e sandbox|production]
   ```

2. List orders from the past X hours:
   ```bash
   ./revcli order list [hours] [-e sandbox|production]
   ```

3. Get order details:
   ```bash
   ./revcli order get <id> [-e sandbox|production]
   ```

4. Update an order:
   ```bash
   ./revcli order update <id> <amount> <currency> [-e sandbox|production]
   ```

5. Capture an order:
   ```bash
   ./revcli order capture <id> [-e sandbox|production]
   ```

6. Cancel an order:
   ```bash
   ./revcli order cancel <id> [-e sandbox|production]
   ```

7. Refund an order:
   ```bash
   ./revcli order refund <id> <amount> [-e sandbox|production]
   ```

8. Pay for an order using a saved payment method:
   ```bash
   ./revcli order pay <id> <payment_method_id> [-e sandbox|production]
   ```

9. Get order payments:
   ```bash
   ./revcli order payments <id> [-e sandbox|production]
   ```

### Options

- `-e, --env <env>`: Environment (sandbox|production, default: production)
- `-h, --help`: Show help message

### Examples

1. List all webhooks in sandbox environment:
   ```bash
   ./revcli webhook list -e sandbox
   ```

2. Register a new webhook:
   ```bash
   ./revcli webhook register https://your-domain.com/webhook -e sandbox
   ```

3. Delete all webhooks in sandbox environment:
   ```bash
   ./revcli webhook purge -e sandbox
   ```

4. Create a new order for 100 EUR:
   ```bash
   ./revcli order create 100 EUR
   ```

5. List orders from the past 24 hours:
   ```bash
   ./revcli order list 24
   ```

6. Get details for a specific order:
   ```bash
   ./revcli order get order_123
   ```

7. Update an order amount:
   ```bash
   ./revcli order update order_123 150 EUR
   ```

8. Capture an authorized order:
   ```bash
   ./revcli order capture order_123
   ```

9. Cancel an uncaptured order:
   ```bash
   ./revcli order cancel order_123
   ```

10. Refund a completed order:
    ```bash
    ./revcli order refund order_123 100
    ```

11. Pay for an order using a saved payment method:
    ```bash
    ./revcli order pay order_123 pm_456
    ```

12. List payments for an order:
    ```bash
    ./revcli order payments order_123
    ```

## Error Handling

The script includes comprehensive error handling for:
- Missing required parameters
- Invalid command values
- Invalid environment values
- Missing API key files
- Invalid hours parameter

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository. 