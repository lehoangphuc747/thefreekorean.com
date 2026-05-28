$secrets = @{
    "FIREBASE_PRIVATE_KEY_ID" = "48f2d02e303386a752f58aed657d9de8e86ecea1"
    "FIREBASE_PRIVATE_KEY" = "-----BEGIN PRIVATE KEY-----`nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmzFNYDiA/MGNZ`nfPW6XXAQdYGqUE25XriTGKzS52TfPOmRlRV4Qn/ZKalEGXuwjyE+T1WKuHoyJRmj`n00t7zd8U2rBQ+1Wb16ISIi7x5IGjD+ABxIzpth8TDDGmZPvw2hr4+OqmO9XpPxEy`ntPJOyZ8Fgpo7D/3JUdTZYC1udFV1LPT59xalSCv0zWoEDHhKqrVzrbHA0MY80FHG`nWK/mqJyDqVFKKANigmWQt1q//ryiVCeKWnohPfNtyDB4b0E4mObal7mQv14sFsGG`nYPzQZKKNVig195CUHSZpC/j8J0wSBSQTXgjhF7gY8O1tjvyCNKfpAUUi3q7Qv3gS`nsMiDhkKXAgMBAAECggEACpXG6DylQT1R4Lj0YypQ1UqPuv4zoILpVbRoK04x8ZTN`nAccjQKl/sYlaS48OcWrz4h9ov0/ruUjvcp0TGj07Xfhu3gTFLwmlKF9w+TrWG0ID`npjR9Dbxi+TnNbcM4gEFWy14vqnnblDpR32CLwvOgqwCG6NtKJx/1HetCmhpj/D7`nM0FBIWT0O1VH7iJRMxur4LBqXvcNhy9lU53MrL4+maXbninYFrLuGIuR1PZIZ9qA`nIeLx6FOvCg7drkKx2aa9TKy2SAJiyG60IrBL4mLLJFn+YEh+GXjbn+jmLGTKVdO4`n9W/hCKV6aBSWRDQCf/+swm0tyGTvQvbP3AIpwQpDmQKBgQDTAnWtbYUJHDsxy0Ys`ngTN+OxKMSqpqSludsncWtEEvVm3y1WET5XSZ+n6xdf+pNMVdYgkTgtTVlA0MMhUH`nxZFMBweua+h6N/4wMb1MvvREFVN73nQK8EOFtwqp06s7KXms9lvMPB/g2JH9aIDX`nnrZeHkTsFIY/oZdtmW73cvNjpQKBgQDKXKvMJ9CT5tHpOTCzemCwJq0N/H6Yn7uk`nkMPZq9qCitODI/2kDWUm5w+0hUPeqx3m4QjXnSSll2Hn0lztClpV3Hy38OixLuky`nwrtJ+IeaiSzqXti/7uLa0N9jZCHIut5kBaDkZ/+3ZN9Q+qLAfqiHVsXv8wh/cMSF`nKQ1DyZoIiwKBgHDZven0ytOmf5oP5wXiS5HVMgRJ4n5aKklaqwo/eSVCCid3KyYi`n74tyRtPOEd+C05Mv3T7MF9vqBFhjaI/xf9WzZM5J89l5nL5Vu7IR5j2LUkzLGjDH`ncrVOwas2Azvu4J46W7oM5dewu9NVUqL+xPXtJltEVtAtMflxt8ErfzPpAoGBAJrF`nPfArE2/LPgiuYP0kQAb5zanAz+JTaOR4hBJbSghFvXezcy6hwBd86Zobwsju/zOy`nMV0XJwwvOAZh8gipvmWk+Q6GBrJdOqZEIZJ1ruEWwW+Pkx9YydCpp/EQiHZJ1gWR`n+Hg4wm+1iscYqpmnRaYdS841hu5RhTyDJU4PRuv5AoGAUi8BwBwZ4PLCS5WyLyIL`nR/r6Ok22AcZb6YnH/k5mCqzkfDcelPO5YifCA3f8tFZZxEG4OzoNdNA+UIZumXRU`n6O9oJ2iJteWgtj2h7Y4meODA3Zr49FhDcTS+04ARqmNaJ3YkiorMF9z6q9x7ZeIq`nBlBlsxBMsgK+BN4+fFxZpwc=`n-----END PRIVATE KEY-----"
    "FIREBASE_PROJECT_ID" = "thefreekorean"
    "FIREBASE_CLIENT_EMAIL" = "firebase-adminsdk-fbsvc@thefreekorean.iam.gserviceaccount.com"
    "FIREBASE_CLIENT_ID" = "113361853815373763585"
    "FIREBASE_AUTH_URI" = "https://accounts.google.com/o/oauth2/auth"
    "FIREBASE_TOKEN_URI" = "https://oauth2.googleapis.com/token"
    "FIREBASE_AUTH_CERT_URL" = "https://www.googleapis.com/oauth2/v1/certs"
    "FIREBASE_CLIENT_CERT_URL" = "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40thefreekorean.iam.gserviceaccount.com"
}

foreach ($key in $secrets.Keys) {
    Write-Host "Setting secret: $key"
    $secrets[$key] | npx wrangler secret put $key
}
