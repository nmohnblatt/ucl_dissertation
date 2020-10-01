# COMP0064 UCL MSc Dissertation

## Privacy-Preserving Contact Discovery with Applications to End-to-End Encrypted Messaging and Mobile-First Cryptocurrencies

Please download `main.pdf` to read the full report.

### Abstract
In this report we consider means to perform privacy-preserving contact discovery on mobile devices. Contact discovery is a crucial initial step for any social application. Current methods reveal private information or require users to reason about cryptography. We introduce an approach based on non-interactive identity-based key exchange protocols (NI-IBKE). Our scheme provides users with cryptographic material which is entirely managed by a client-side application. Users can input their contacts’ phone numbers (or an equivalent human-readable identifier) to compute shared secret keys on-device. Our system relies on a t-out-of-n trust assumption with respect to a decentralised service. We show that the desired privacy property holds in the random oracle model under the decisional bilinear Diffie-Hellman assumption. We provide estimates of the system’s performance in the wild. These show that our scheme is applicable but will require optimisations or a long bootstrapping period if used for applications with billions of users. Finally we describe a simple proof-of-concept implementation as well as applications of the scheme for end-to-end messaging or mobile-first cryptocurrencies.

### Implementation 
See [proof-of-concept](https://github.com/nmohnblatt/cd_client) implemented in Go using the [kyber library](https://github.com/dedis/kyber).

