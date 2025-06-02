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

## Development Tips

### Setting Up a Sandbox Merchant Account

1. Register a sandbox account at [sandbox-business.revolut.com/signup](https://sandbox-business.revolut.com/signup)
2. Once logged in, go to Settings (cogwheel) → APIs → Merchant account
3. Generate your API key and save it in `revolut.sandbox.secret.key`

### Testing Webhooks with ngrok

When developing locally, you can use ngrok to receive webhooks. This repository includes a simple webhook listener that helps you debug incoming requests.

1. Install ngrok:
   ```bash
   # macOS
   brew install ngrok
   
   # Linux
   snap install ngrok
   ```

2. Start the webhook listener in one terminal:
   ```bash
   # Install Flask if you haven't already
   pip install flask
   
   # Run the listener
   python webhook_listener.py
   ```
   You should see: "Starting webhook listener on http://localhost:8000"

3. Start ngrok in another terminal:
   ```bash
   ngrok http 8000
   ```
   You'll see a display showing your public URL (e.g., `https://abc123.ngrok.io`)

4. Register the webhook with Revolut:
   ```bash
   ./revcli webhook register https://abc123.ngrok.io/webhook -e sandbox
   ```

5. Test the webhook by creating a test order:
   ```bash
   ./revcli order create 100 EUR -e sandbox
   ```

6. Watch the webhook listener terminal - you'll see the incoming request details:
   ```
   === New Request at 2024-03-21 15:30:45 ===
   Method: POST
   URL: https://abc123.ngrok.io/webhook
   Path: /webhook
   Query Params: {}
   Headers: {
     "Content-Type": "application/json",
     "User-Agent": "Revolut-Webhook/1.0",
     "X-Revolut-Signature": "sha256=..."
   }
   Body: {
     "event": "ORDER_PAYMENT_COMPLETED",
     "order_id": "order_123",
     "payment_id": "pay_456"
   }
   ==================================================
   ```

The webhook listener will help you:
- Verify webhook delivery
- Inspect request headers and signatures
- Debug payload structure
- Test different webhook events

Note: The ngrok URL changes each time you restart ngrok unless you have a paid account. Make sure to update your webhook URL in Revolut when this happens.

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