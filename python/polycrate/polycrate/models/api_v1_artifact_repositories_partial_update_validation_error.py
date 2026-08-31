from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_repositories_partial_update_alternative_repository_url_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_annotations_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_archived_at_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_archived_by_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_archived_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_archived_reason_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_created_by_component_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_created_by_user_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_credential_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_criticality_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_debug_mode_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_display_name_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_kind_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_labels_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_managed_by_content_type_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_managed_by_object_id_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_modified_by_user_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_name_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_non_field_errors_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_platform_service_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_provider_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_provider_id_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_provider_reference_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_repository_url_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_sla_availability_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_sla_target_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_sla_window_days_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_slo_availability_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_slo_target_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_slo_window_days_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_target_availability_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_partial_update_tolerations_error_component import (
        ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactRepositoriesPartialUpdateValidationError")


@_attrs_define
class ApiV1ArtifactRepositoriesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_repositories_partial_update_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_annotations_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_at_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_by_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_criticality_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_display_name_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_kind_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_labels_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_name_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_platform_service_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_id_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_repository_url_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_target_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_target_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_target_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_tolerations_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent):
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
        from ..models.api_v1_artifact_repositories_partial_update_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_annotations_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_at_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_by_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_credential_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_criticality_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_display_name_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_kind_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_labels_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_name_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_platform_service_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_id_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_repository_url_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_target_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_target_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_target_availability_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_partial_update_tolerations_error_component import (
            ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_0 = (
                        ApiV1ArtifactRepositoriesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_1 = (
                        ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_2 = (
                        ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_3 = (
                        ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_4 = (
                        ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_5 = (
                        ApiV1ArtifactRepositoriesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_6 = (
                        ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_7 = (
                        ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_8 = (
                        ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_9 = (
                        ApiV1ArtifactRepositoriesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_10 = (
                        ApiV1ArtifactRepositoriesPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_11 = (
                        ApiV1ArtifactRepositoriesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_12 = (
                        ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_13 = (
                        ApiV1ArtifactRepositoriesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_14 = (
                        ApiV1ArtifactRepositoriesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_15 = (
                        ApiV1ArtifactRepositoriesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_16 = (
                        ApiV1ArtifactRepositoriesPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_17 = (
                        ApiV1ArtifactRepositoriesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_18 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_19 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_20 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_21 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_22 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_23 = (
                        ApiV1ArtifactRepositoriesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_24 = (
                        ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_25 = (
                        ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_26 = (
                        ApiV1ArtifactRepositoriesPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_27 = (
                        ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_28 = (
                        ApiV1ArtifactRepositoriesPartialUpdateRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_29 = (
                        ApiV1ArtifactRepositoriesPartialUpdateAlternativeRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_30 = (
                        ApiV1ArtifactRepositoriesPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_31 = (
                        ApiV1ArtifactRepositoriesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_32 = (
                        ApiV1ArtifactRepositoriesPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_partial_update_error_type_33 = (
                        ApiV1ArtifactRepositoriesPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_repositories_partial_update_error_type_34 = (
                    ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_repositories_partial_update_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_repositories_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_repositories_partial_update_validation_error.additional_properties = d
        return api_v1_artifact_repositories_partial_update_validation_error

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
