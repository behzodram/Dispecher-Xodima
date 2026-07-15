import os
from datetime import timedelta

from livekit import api

from config import (
    LIVEKIT_API_KEY,
    LIVEKIT_API_SECRET,
    LIVEKIT_URL,
)


def create_access_token(identity: str, room_name: str) -> dict:
    token = (
        api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
        .with_identity(identity)
        .with_name(identity)
        .with_grants(
            api.VideoGrants(
                room_join=True,
                room=room_name,
            )
        )
        .to_jwt()
    )

    return {
        "success": True,
        "livekit_url": LIVEKIT_URL,
        "token": token,
        "expires_in": int(timedelta(hours=1).total_seconds()),
    }