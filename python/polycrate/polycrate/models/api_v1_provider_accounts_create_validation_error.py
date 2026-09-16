from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_provider_accounts_create_annotations_error_component import (
        ApiV1ProviderAccountsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_api_backoff_minutes_error_component import (
        ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_api_endpoint_error_component import (
        ApiV1ProviderAccountsCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_api_kind_error_component import (
        ApiV1ProviderAccountsCreateApiKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_archived_at_error_component import (
        ApiV1ProviderAccountsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_archived_by_error_component import (
        ApiV1ProviderAccountsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_archived_error_component import (
        ApiV1ProviderAccountsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_archived_reason_error_component import (
        ApiV1ProviderAccountsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_created_by_component_error_component import (
        ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_created_by_user_error_component import (
        ApiV1ProviderAccountsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_credential_id_error_component import (
        ApiV1ProviderAccountsCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_criticality_error_component import (
        ApiV1ProviderAccountsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_debug_mode_error_component import (
        ApiV1ProviderAccountsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_display_name_error_component import (
        ApiV1ProviderAccountsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_kind_error_component import (
        ApiV1ProviderAccountsCreateKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_labels_error_component import (
        ApiV1ProviderAccountsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_last_rate_limited_at_error_component import (
        ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_managed_by_content_type_error_component import (
        ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_managed_by_object_id_error_component import (
        ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_metadata_error_component import (
        ApiV1ProviderAccountsCreateMetadataErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_modified_by_user_error_component import (
        ApiV1ProviderAccountsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_name_error_component import (
        ApiV1ProviderAccountsCreateNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_non_field_errors_error_component import (
        ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_organization_id_error_component import (
        ApiV1ProviderAccountsCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_platform_dns_record_created_error_component import (
        ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_platform_service_error_component import (
        ApiV1ProviderAccountsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_provider_entity_id_error_component import (
        ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_provider_error_component import (
        ApiV1ProviderAccountsCreateProviderErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_provider_id_error_component import (
        ApiV1ProviderAccountsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_provider_reference_error_component import (
        ApiV1ProviderAccountsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_reconciliation_enabled_error_component import (
        ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_sla_availability_error_component import (
        ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_sla_target_error_component import (
        ApiV1ProviderAccountsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_sla_window_days_error_component import (
        ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_slo_availability_error_component import (
        ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_slo_target_error_component import (
        ApiV1ProviderAccountsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_slo_window_days_error_component import (
        ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_target_availability_error_component import (
        ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_tolerations_error_component import (
        ApiV1ProviderAccountsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_create_workspace_id_error_component import (
        ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProviderAccountsCreateValidationError")


@_attrs_define
class ApiV1ProviderAccountsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProviderAccountsCreateAnnotationsErrorComponent |
            ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent |
            ApiV1ProviderAccountsCreateApiEndpointErrorComponent | ApiV1ProviderAccountsCreateApiKindErrorComponent |
            ApiV1ProviderAccountsCreateArchivedAtErrorComponent | ApiV1ProviderAccountsCreateArchivedByErrorComponent |
            ApiV1ProviderAccountsCreateArchivedErrorComponent | ApiV1ProviderAccountsCreateArchivedReasonErrorComponent |
            ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent |
            ApiV1ProviderAccountsCreateCreatedByUserErrorComponent | ApiV1ProviderAccountsCreateCredentialIdErrorComponent |
            ApiV1ProviderAccountsCreateCriticalityErrorComponent | ApiV1ProviderAccountsCreateDebugModeErrorComponent |
            ApiV1ProviderAccountsCreateDisplayNameErrorComponent | ApiV1ProviderAccountsCreateKindErrorComponent |
            ApiV1ProviderAccountsCreateLabelsErrorComponent | ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent |
            ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent |
            ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent | ApiV1ProviderAccountsCreateMetadataErrorComponent |
            ApiV1ProviderAccountsCreateModifiedByUserErrorComponent | ApiV1ProviderAccountsCreateNameErrorComponent |
            ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent |
            ApiV1ProviderAccountsCreateOrganizationIdErrorComponent |
            ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ProviderAccountsCreatePlatformServiceErrorComponent |
            ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent | ApiV1ProviderAccountsCreateProviderErrorComponent |
            ApiV1ProviderAccountsCreateProviderIdErrorComponent | ApiV1ProviderAccountsCreateProviderReferenceErrorComponent
            | ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent |
            ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent | ApiV1ProviderAccountsCreateSlaTargetErrorComponent |
            ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent |
            ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent | ApiV1ProviderAccountsCreateSloTargetErrorComponent |
            ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent |
            ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent |
            ApiV1ProviderAccountsCreateTolerationsErrorComponent | ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProviderAccountsCreateAnnotationsErrorComponent
        | ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent
        | ApiV1ProviderAccountsCreateApiEndpointErrorComponent
        | ApiV1ProviderAccountsCreateApiKindErrorComponent
        | ApiV1ProviderAccountsCreateArchivedAtErrorComponent
        | ApiV1ProviderAccountsCreateArchivedByErrorComponent
        | ApiV1ProviderAccountsCreateArchivedErrorComponent
        | ApiV1ProviderAccountsCreateArchivedReasonErrorComponent
        | ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent
        | ApiV1ProviderAccountsCreateCreatedByUserErrorComponent
        | ApiV1ProviderAccountsCreateCredentialIdErrorComponent
        | ApiV1ProviderAccountsCreateCriticalityErrorComponent
        | ApiV1ProviderAccountsCreateDebugModeErrorComponent
        | ApiV1ProviderAccountsCreateDisplayNameErrorComponent
        | ApiV1ProviderAccountsCreateKindErrorComponent
        | ApiV1ProviderAccountsCreateLabelsErrorComponent
        | ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent
        | ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent
        | ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent
        | ApiV1ProviderAccountsCreateMetadataErrorComponent
        | ApiV1ProviderAccountsCreateModifiedByUserErrorComponent
        | ApiV1ProviderAccountsCreateNameErrorComponent
        | ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent
        | ApiV1ProviderAccountsCreateOrganizationIdErrorComponent
        | ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ProviderAccountsCreatePlatformServiceErrorComponent
        | ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent
        | ApiV1ProviderAccountsCreateProviderErrorComponent
        | ApiV1ProviderAccountsCreateProviderIdErrorComponent
        | ApiV1ProviderAccountsCreateProviderReferenceErrorComponent
        | ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent
        | ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent
        | ApiV1ProviderAccountsCreateSlaTargetErrorComponent
        | ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent
        | ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent
        | ApiV1ProviderAccountsCreateSloTargetErrorComponent
        | ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent
        | ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent
        | ApiV1ProviderAccountsCreateTolerationsErrorComponent
        | ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_provider_accounts_create_annotations_error_component import (
            ApiV1ProviderAccountsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_endpoint_error_component import (
            ApiV1ProviderAccountsCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_kind_error_component import (
            ApiV1ProviderAccountsCreateApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_at_error_component import (
            ApiV1ProviderAccountsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_by_error_component import (
            ApiV1ProviderAccountsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_error_component import (
            ApiV1ProviderAccountsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_reason_error_component import (
            ApiV1ProviderAccountsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_created_by_component_error_component import (
            ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_credential_id_error_component import (
            ApiV1ProviderAccountsCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_criticality_error_component import (
            ApiV1ProviderAccountsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_debug_mode_error_component import (
            ApiV1ProviderAccountsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_display_name_error_component import (
            ApiV1ProviderAccountsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_kind_error_component import (
            ApiV1ProviderAccountsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_labels_error_component import (
            ApiV1ProviderAccountsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_metadata_error_component import (
            ApiV1ProviderAccountsCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_modified_by_user_error_component import (
            ApiV1ProviderAccountsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_name_error_component import (
            ApiV1ProviderAccountsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_non_field_errors_error_component import (
            ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_organization_id_error_component import (
            ApiV1ProviderAccountsCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_platform_service_error_component import (
            ApiV1ProviderAccountsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_entity_id_error_component import (
            ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_error_component import (
            ApiV1ProviderAccountsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_id_error_component import (
            ApiV1ProviderAccountsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_reference_error_component import (
            ApiV1ProviderAccountsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_availability_error_component import (
            ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_target_error_component import (
            ApiV1ProviderAccountsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_window_days_error_component import (
            ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_availability_error_component import (
            ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_target_error_component import (
            ApiV1ProviderAccountsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_window_days_error_component import (
            ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_target_availability_error_component import (
            ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_tolerations_error_component import (
            ApiV1ProviderAccountsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_workspace_id_error_component import (
            ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateApiKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_provider_accounts_create_annotations_error_component import (
            ApiV1ProviderAccountsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_endpoint_error_component import (
            ApiV1ProviderAccountsCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_api_kind_error_component import (
            ApiV1ProviderAccountsCreateApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_at_error_component import (
            ApiV1ProviderAccountsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_by_error_component import (
            ApiV1ProviderAccountsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_error_component import (
            ApiV1ProviderAccountsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_archived_reason_error_component import (
            ApiV1ProviderAccountsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_created_by_component_error_component import (
            ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_created_by_user_error_component import (
            ApiV1ProviderAccountsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_credential_id_error_component import (
            ApiV1ProviderAccountsCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_criticality_error_component import (
            ApiV1ProviderAccountsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_debug_mode_error_component import (
            ApiV1ProviderAccountsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_display_name_error_component import (
            ApiV1ProviderAccountsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_kind_error_component import (
            ApiV1ProviderAccountsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_labels_error_component import (
            ApiV1ProviderAccountsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_metadata_error_component import (
            ApiV1ProviderAccountsCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_modified_by_user_error_component import (
            ApiV1ProviderAccountsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_name_error_component import (
            ApiV1ProviderAccountsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_non_field_errors_error_component import (
            ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_organization_id_error_component import (
            ApiV1ProviderAccountsCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_platform_service_error_component import (
            ApiV1ProviderAccountsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_entity_id_error_component import (
            ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_error_component import (
            ApiV1ProviderAccountsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_id_error_component import (
            ApiV1ProviderAccountsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_provider_reference_error_component import (
            ApiV1ProviderAccountsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_availability_error_component import (
            ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_target_error_component import (
            ApiV1ProviderAccountsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_sla_window_days_error_component import (
            ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_availability_error_component import (
            ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_target_error_component import (
            ApiV1ProviderAccountsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_slo_window_days_error_component import (
            ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_target_availability_error_component import (
            ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_tolerations_error_component import (
            ApiV1ProviderAccountsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_create_workspace_id_error_component import (
            ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProviderAccountsCreateAnnotationsErrorComponent
                | ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent
                | ApiV1ProviderAccountsCreateApiEndpointErrorComponent
                | ApiV1ProviderAccountsCreateApiKindErrorComponent
                | ApiV1ProviderAccountsCreateArchivedAtErrorComponent
                | ApiV1ProviderAccountsCreateArchivedByErrorComponent
                | ApiV1ProviderAccountsCreateArchivedErrorComponent
                | ApiV1ProviderAccountsCreateArchivedReasonErrorComponent
                | ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent
                | ApiV1ProviderAccountsCreateCreatedByUserErrorComponent
                | ApiV1ProviderAccountsCreateCredentialIdErrorComponent
                | ApiV1ProviderAccountsCreateCriticalityErrorComponent
                | ApiV1ProviderAccountsCreateDebugModeErrorComponent
                | ApiV1ProviderAccountsCreateDisplayNameErrorComponent
                | ApiV1ProviderAccountsCreateKindErrorComponent
                | ApiV1ProviderAccountsCreateLabelsErrorComponent
                | ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent
                | ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent
                | ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent
                | ApiV1ProviderAccountsCreateMetadataErrorComponent
                | ApiV1ProviderAccountsCreateModifiedByUserErrorComponent
                | ApiV1ProviderAccountsCreateNameErrorComponent
                | ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent
                | ApiV1ProviderAccountsCreateOrganizationIdErrorComponent
                | ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ProviderAccountsCreatePlatformServiceErrorComponent
                | ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent
                | ApiV1ProviderAccountsCreateProviderErrorComponent
                | ApiV1ProviderAccountsCreateProviderIdErrorComponent
                | ApiV1ProviderAccountsCreateProviderReferenceErrorComponent
                | ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent
                | ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent
                | ApiV1ProviderAccountsCreateSlaTargetErrorComponent
                | ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent
                | ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent
                | ApiV1ProviderAccountsCreateSloTargetErrorComponent
                | ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent
                | ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent
                | ApiV1ProviderAccountsCreateTolerationsErrorComponent
                | ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_0 = (
                        ApiV1ProviderAccountsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_1 = (
                        ApiV1ProviderAccountsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_2 = (
                        ApiV1ProviderAccountsCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_3 = (
                        ApiV1ProviderAccountsCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_4 = (
                        ApiV1ProviderAccountsCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_5 = (
                        ApiV1ProviderAccountsCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_6 = (
                        ApiV1ProviderAccountsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_7 = (
                        ApiV1ProviderAccountsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_8 = (
                        ApiV1ProviderAccountsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_9 = (
                        ApiV1ProviderAccountsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_10 = (
                        ApiV1ProviderAccountsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_11 = (
                        ApiV1ProviderAccountsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_12 = (
                        ApiV1ProviderAccountsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_13 = (
                        ApiV1ProviderAccountsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_14 = (
                        ApiV1ProviderAccountsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_15 = (
                        ApiV1ProviderAccountsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_16 = (
                        ApiV1ProviderAccountsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_17 = (
                        ApiV1ProviderAccountsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_18 = (
                        ApiV1ProviderAccountsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_19 = (
                        ApiV1ProviderAccountsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_20 = (
                        ApiV1ProviderAccountsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_21 = (
                        ApiV1ProviderAccountsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_22 = (
                        ApiV1ProviderAccountsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_23 = (
                        ApiV1ProviderAccountsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_24 = (
                        ApiV1ProviderAccountsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_25 = (
                        ApiV1ProviderAccountsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_26 = (
                        ApiV1ProviderAccountsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_27 = (
                        ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_28 = (
                        ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_29 = (
                        ApiV1ProviderAccountsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_30 = (
                        ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_31 = (
                        ApiV1ProviderAccountsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_32 = (
                        ApiV1ProviderAccountsCreateApiKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_33 = (
                        ApiV1ProviderAccountsCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_34 = (
                        ApiV1ProviderAccountsCreateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_35 = (
                        ApiV1ProviderAccountsCreateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_36 = (
                        ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_37 = (
                        ApiV1ProviderAccountsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_38 = (
                        ApiV1ProviderAccountsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_create_error_type_39 = (
                        ApiV1ProviderAccountsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_provider_accounts_create_error_type_40 = (
                    ApiV1ProviderAccountsCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_provider_accounts_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_provider_accounts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_provider_accounts_create_validation_error.additional_properties = d
        return api_v1_provider_accounts_create_validation_error

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
