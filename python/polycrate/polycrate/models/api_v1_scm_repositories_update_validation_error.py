from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_scm_repositories_update_annotations_error_component import (
        ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_archived_at_error_component import (
        ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_archived_error_component import (
        ApiV1ScmRepositoriesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_archived_reason_error_component import (
        ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_credential_error_component import (
        ApiV1ScmRepositoriesUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_criticality_error_component import (
        ApiV1ScmRepositoriesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_debug_mode_error_component import (
        ApiV1ScmRepositoriesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_display_name_error_component import (
        ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_groups_count_error_component import (
        ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_hostname_error_component import (
        ApiV1ScmRepositoriesUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_k8s_app_error_component import (
        ApiV1ScmRepositoriesUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_k8s_cluster_error_component import (
        ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_kind_error_component import (
        ApiV1ScmRepositoriesUpdateKindErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_labels_error_component import (
        ApiV1ScmRepositoriesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_metadata_error_component import (
        ApiV1ScmRepositoriesUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_name_error_component import (
        ApiV1ScmRepositoriesUpdateNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_non_field_errors_error_component import (
        ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_platform_service_error_component import (
        ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_projects_count_error_component import (
        ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_provider_error_component import (
        ApiV1ScmRepositoriesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_provider_id_error_component import (
        ApiV1ScmRepositoriesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_provider_reference_error_component import (
        ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_reconciliation_enabled_error_component import (
        ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_repository_version_error_component import (
        ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_sla_availability_error_component import (
        ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_sla_target_error_component import (
        ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_slo_availability_error_component import (
        ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_slo_target_error_component import (
        ApiV1ScmRepositoriesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_target_availability_error_component import (
        ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_tolerations_error_component import (
        ApiV1ScmRepositoriesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_update_users_count_error_component import (
        ApiV1ScmRepositoriesUpdateUsersCountErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ScmRepositoriesUpdateValidationError")


@_attrs_define
class ApiV1ScmRepositoriesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent |
            ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent | ApiV1ScmRepositoriesUpdateArchivedErrorComponent |
            ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent | ApiV1ScmRepositoriesUpdateCredentialErrorComponent |
            ApiV1ScmRepositoriesUpdateCriticalityErrorComponent | ApiV1ScmRepositoriesUpdateDebugModeErrorComponent |
            ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent | ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent |
            ApiV1ScmRepositoriesUpdateHostnameErrorComponent | ApiV1ScmRepositoriesUpdateK8SAppErrorComponent |
            ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent | ApiV1ScmRepositoriesUpdateKindErrorComponent |
            ApiV1ScmRepositoriesUpdateLabelsErrorComponent | ApiV1ScmRepositoriesUpdateMetadataErrorComponent |
            ApiV1ScmRepositoriesUpdateNameErrorComponent | ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent |
            ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent | ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent
            | ApiV1ScmRepositoriesUpdateProviderErrorComponent | ApiV1ScmRepositoriesUpdateProviderIdErrorComponent |
            ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent |
            ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent |
            ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent |
            ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent | ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent |
            ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent | ApiV1ScmRepositoriesUpdateSloTargetErrorComponent |
            ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent | ApiV1ScmRepositoriesUpdateTolerationsErrorComponent
            | ApiV1ScmRepositoriesUpdateUsersCountErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent
        | ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent
        | ApiV1ScmRepositoriesUpdateArchivedErrorComponent
        | ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent
        | ApiV1ScmRepositoriesUpdateCredentialErrorComponent
        | ApiV1ScmRepositoriesUpdateCriticalityErrorComponent
        | ApiV1ScmRepositoriesUpdateDebugModeErrorComponent
        | ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent
        | ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent
        | ApiV1ScmRepositoriesUpdateHostnameErrorComponent
        | ApiV1ScmRepositoriesUpdateK8SAppErrorComponent
        | ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent
        | ApiV1ScmRepositoriesUpdateKindErrorComponent
        | ApiV1ScmRepositoriesUpdateLabelsErrorComponent
        | ApiV1ScmRepositoriesUpdateMetadataErrorComponent
        | ApiV1ScmRepositoriesUpdateNameErrorComponent
        | ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent
        | ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent
        | ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent
        | ApiV1ScmRepositoriesUpdateProviderErrorComponent
        | ApiV1ScmRepositoriesUpdateProviderIdErrorComponent
        | ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent
        | ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent
        | ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent
        | ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent
        | ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent
        | ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent
        | ApiV1ScmRepositoriesUpdateSloTargetErrorComponent
        | ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent
        | ApiV1ScmRepositoriesUpdateTolerationsErrorComponent
        | ApiV1ScmRepositoriesUpdateUsersCountErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_scm_repositories_update_annotations_error_component import (
            ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_at_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_reason_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_credential_error_component import (
            ApiV1ScmRepositoriesUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_criticality_error_component import (
            ApiV1ScmRepositoriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_debug_mode_error_component import (
            ApiV1ScmRepositoriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_display_name_error_component import (
            ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_groups_count_error_component import (
            ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_hostname_error_component import (
            ApiV1ScmRepositoriesUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_k8s_app_error_component import (
            ApiV1ScmRepositoriesUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_kind_error_component import (
            ApiV1ScmRepositoriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_labels_error_component import (
            ApiV1ScmRepositoriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_name_error_component import (
            ApiV1ScmRepositoriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_non_field_errors_error_component import (
            ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_platform_service_error_component import (
            ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_projects_count_error_component import (
            ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_error_component import (
            ApiV1ScmRepositoriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_id_error_component import (
            ApiV1ScmRepositoriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_reference_error_component import (
            ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_repository_version_error_component import (
            ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_sla_availability_error_component import (
            ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_sla_target_error_component import (
            ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_slo_availability_error_component import (
            ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_slo_target_error_component import (
            ApiV1ScmRepositoriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_target_availability_error_component import (
            ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_tolerations_error_component import (
            ApiV1ScmRepositoriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_users_count_error_component import (
            ApiV1ScmRepositoriesUpdateUsersCountErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateUsersCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_scm_repositories_update_annotations_error_component import (
            ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_at_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_archived_reason_error_component import (
            ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_credential_error_component import (
            ApiV1ScmRepositoriesUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_criticality_error_component import (
            ApiV1ScmRepositoriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_debug_mode_error_component import (
            ApiV1ScmRepositoriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_display_name_error_component import (
            ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_groups_count_error_component import (
            ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_hostname_error_component import (
            ApiV1ScmRepositoriesUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_k8s_app_error_component import (
            ApiV1ScmRepositoriesUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_kind_error_component import (
            ApiV1ScmRepositoriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_labels_error_component import (
            ApiV1ScmRepositoriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_metadata_error_component import (
            ApiV1ScmRepositoriesUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_name_error_component import (
            ApiV1ScmRepositoriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_non_field_errors_error_component import (
            ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_platform_service_error_component import (
            ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_projects_count_error_component import (
            ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_error_component import (
            ApiV1ScmRepositoriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_id_error_component import (
            ApiV1ScmRepositoriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_provider_reference_error_component import (
            ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_repository_version_error_component import (
            ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_sla_availability_error_component import (
            ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_sla_target_error_component import (
            ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_slo_availability_error_component import (
            ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_slo_target_error_component import (
            ApiV1ScmRepositoriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_target_availability_error_component import (
            ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_tolerations_error_component import (
            ApiV1ScmRepositoriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_update_users_count_error_component import (
            ApiV1ScmRepositoriesUpdateUsersCountErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent
                | ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent
                | ApiV1ScmRepositoriesUpdateArchivedErrorComponent
                | ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent
                | ApiV1ScmRepositoriesUpdateCredentialErrorComponent
                | ApiV1ScmRepositoriesUpdateCriticalityErrorComponent
                | ApiV1ScmRepositoriesUpdateDebugModeErrorComponent
                | ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent
                | ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent
                | ApiV1ScmRepositoriesUpdateHostnameErrorComponent
                | ApiV1ScmRepositoriesUpdateK8SAppErrorComponent
                | ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent
                | ApiV1ScmRepositoriesUpdateKindErrorComponent
                | ApiV1ScmRepositoriesUpdateLabelsErrorComponent
                | ApiV1ScmRepositoriesUpdateMetadataErrorComponent
                | ApiV1ScmRepositoriesUpdateNameErrorComponent
                | ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent
                | ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent
                | ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent
                | ApiV1ScmRepositoriesUpdateProviderErrorComponent
                | ApiV1ScmRepositoriesUpdateProviderIdErrorComponent
                | ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent
                | ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent
                | ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent
                | ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent
                | ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent
                | ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent
                | ApiV1ScmRepositoriesUpdateSloTargetErrorComponent
                | ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent
                | ApiV1ScmRepositoriesUpdateTolerationsErrorComponent
                | ApiV1ScmRepositoriesUpdateUsersCountErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_0 = (
                        ApiV1ScmRepositoriesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_1 = (
                        ApiV1ScmRepositoriesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_2 = (
                        ApiV1ScmRepositoriesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_3 = (
                        ApiV1ScmRepositoriesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_4 = (
                        ApiV1ScmRepositoriesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_5 = (
                        ApiV1ScmRepositoriesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_6 = (
                        ApiV1ScmRepositoriesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_7 = (
                        ApiV1ScmRepositoriesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_8 = (
                        ApiV1ScmRepositoriesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_9 = (
                        ApiV1ScmRepositoriesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_10 = (
                        ApiV1ScmRepositoriesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_11 = (
                        ApiV1ScmRepositoriesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_12 = (
                        ApiV1ScmRepositoriesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_13 = (
                        ApiV1ScmRepositoriesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_14 = (
                        ApiV1ScmRepositoriesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_15 = (
                        ApiV1ScmRepositoriesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_16 = (
                        ApiV1ScmRepositoriesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_17 = (
                        ApiV1ScmRepositoriesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_18 = (
                        ApiV1ScmRepositoriesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_19 = (
                        ApiV1ScmRepositoriesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_20 = (
                        ApiV1ScmRepositoriesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_21 = (
                        ApiV1ScmRepositoriesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_22 = (
                        ApiV1ScmRepositoriesUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_23 = (
                        ApiV1ScmRepositoriesUpdateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_24 = (
                        ApiV1ScmRepositoriesUpdateUsersCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_25 = (
                        ApiV1ScmRepositoriesUpdateGroupsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_26 = (
                        ApiV1ScmRepositoriesUpdateRepositoryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_27 = (
                        ApiV1ScmRepositoriesUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_28 = (
                        ApiV1ScmRepositoriesUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_update_error_type_29 = (
                        ApiV1ScmRepositoriesUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_scm_repositories_update_error_type_30 = (
                    ApiV1ScmRepositoriesUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_scm_repositories_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_scm_repositories_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_scm_repositories_update_validation_error.additional_properties = d
        return api_v1_scm_repositories_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
