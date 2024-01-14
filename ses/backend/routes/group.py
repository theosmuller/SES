from fastapi import APIRouter
from ..service.group import GroupService
from ses.schemas.schemas import Group

router = APIRouter()
groupService = GroupService()


@router.get("/groups/{group_name}")
def get_group_by_name(group_name: str):
    return groupService.get_group_by_name(group_name)

@router.get("/groups/remote")
def get_all_remote_groups():
    return groupService.get_groups_by_remote(True)
    
@router.post("/groups")
def add_group(group: Group):
    return groupService.add_group(group)
