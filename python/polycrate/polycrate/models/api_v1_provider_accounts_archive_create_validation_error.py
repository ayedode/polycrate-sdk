from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_provider_accounts_archive_create_annotations_error_component import (
        ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_api_backoff_minutes_error_component import (
        ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_api_endpoint_error_component import (
        ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_api_kind_error_component import (
        ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_archived_at_error_component import (
        ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_archived_by_error_component import (
        ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_archived_error_component import (
        ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_archived_reason_error_component import (
        ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_created_by_component_error_component import (
        ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_created_by_user_error_component import (
        ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_credential_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_criticality_error_component import (
        ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_debug_mode_error_component import (
        ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_display_name_error_component import (
        ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_kind_error_component import (
        ApiV1ProviderAccountsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_labels_error_component import (
        ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_last_rate_limited_at_error_component import (
        ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_managed_by_content_type_error_component import (
        ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_managed_by_object_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_metadata_error_component import (
        ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_modified_by_user_error_component import (
        ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_name_error_component import (
        ApiV1ProviderAccountsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_non_field_errors_error_component import (
        ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_organization_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_platform_dns_record_created_error_component import (
        ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_platform_service_error_component import (
        ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_provider_entity_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_provider_error_component import (
        ApiV1ProviderAccountsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_provider_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_provider_reference_error_component import (
        ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_reconciliation_enabled_error_component import (
        ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_sla_availability_error_component import (
        ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_sla_target_error_component import (
        ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_sla_window_days_error_component import (
        ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_slo_availability_error_component import (
        ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_slo_target_error_component import (
        ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_slo_window_days_error_component import (
        ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_target_availability_error_component import (
        ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_tolerations_error_component import (
        ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_archive_create_workspace_id_error_component import (
        ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProviderAccountsArchiveCreateValidationError")


@_attrs_define
class ApiV1ProviderAccountsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent |
            ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent |
            ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent |
            ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent |
            ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent |
            ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent |
            ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent |
            ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent |
            ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent |
            ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent |
            ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent |
            ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent |
            ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent |
            ApiV1ProviderAccountsArchiveCreateKindErrorComponent | ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent |
            ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent |
            ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent |
            ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent |
            ApiV1ProviderAccountsArchiveCreateNameErrorComponent |
            ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent |
            ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent |
            ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent |
            ApiV1ProviderAccountsArchiveCreateProviderErrorComponent |
            ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent |
            ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent |
            ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent |
            ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent |
            ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent
        | ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent
        | ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent
        | ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent
        | ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent
        | ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent
        | ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent
        | ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent
        | ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent
        | ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent
        | ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent
        | ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent
        | ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent
        | ApiV1ProviderAccountsArchiveCreateKindErrorComponent
        | ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent
        | ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent
        | ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent
        | ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent
        | ApiV1ProviderAccountsArchiveCreateNameErrorComponent
        | ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent
        | ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent
        | ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent
        | ApiV1ProviderAccountsArchiveCreateProviderErrorComponent
        | ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent
        | ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent
        | ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent
        | ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent
        | ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_provider_accounts_archive_create_annotations_error_component import (
            ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_endpoint_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_kind_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_at_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_by_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_reason_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_created_by_component_error_component import (
            ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_credential_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_criticality_error_component import (
            ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_debug_mode_error_component import (
            ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_display_name_error_component import (
            ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_kind_error_component import (
            ApiV1ProviderAccountsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_labels_error_component import (
            ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_metadata_error_component import (
            ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_modified_by_user_error_component import (
            ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_name_error_component import (
            ApiV1ProviderAccountsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_non_field_errors_error_component import (
            ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_organization_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_platform_service_error_component import (
            ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_entity_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_reference_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_target_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_window_days_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_target_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_window_days_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_target_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_tolerations_error_component import (
            ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_workspace_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_provider_accounts_archive_create_annotations_error_component import (
            ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_endpoint_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_api_kind_error_component import (
            ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_at_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_by_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_archived_reason_error_component import (
            ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_created_by_component_error_component import (
            ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_created_by_user_error_component import (
            ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_credential_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_criticality_error_component import (
            ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_debug_mode_error_component import (
            ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_display_name_error_component import (
            ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_kind_error_component import (
            ApiV1ProviderAccountsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_labels_error_component import (
            ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_metadata_error_component import (
            ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_modified_by_user_error_component import (
            ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_name_error_component import (
            ApiV1ProviderAccountsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_non_field_errors_error_component import (
            ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_organization_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_platform_service_error_component import (
            ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_entity_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_provider_reference_error_component import (
            ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_target_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_sla_window_days_error_component import (
            ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_target_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_slo_window_days_error_component import (
            ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_target_availability_error_component import (
            ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_tolerations_error_component import (
            ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_archive_create_workspace_id_error_component import (
            ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent
                | ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent
                | ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent
                | ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent
                | ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent
                | ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent
                | ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent
                | ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent
                | ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent
                | ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent
                | ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent
                | ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent
                | ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent
                | ApiV1ProviderAccountsArchiveCreateKindErrorComponent
                | ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent
                | ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent
                | ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent
                | ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent
                | ApiV1ProviderAccountsArchiveCreateNameErrorComponent
                | ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent
                | ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent
                | ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent
                | ApiV1ProviderAccountsArchiveCreateProviderErrorComponent
                | ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent
                | ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent
                | ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent
                | ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent
                | ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_0 = (
                        ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_1 = (
                        ApiV1ProviderAccountsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_2 = (
                        ApiV1ProviderAccountsArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_3 = (
                        ApiV1ProviderAccountsArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_4 = (
                        ApiV1ProviderAccountsArchiveCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_5 = (
                        ApiV1ProviderAccountsArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_6 = (
                        ApiV1ProviderAccountsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_7 = (
                        ApiV1ProviderAccountsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_8 = (
                        ApiV1ProviderAccountsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_9 = (
                        ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_10 = (
                        ApiV1ProviderAccountsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_11 = (
                        ApiV1ProviderAccountsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_12 = (
                        ApiV1ProviderAccountsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_13 = (
                        ApiV1ProviderAccountsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_14 = (
                        ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_15 = (
                        ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_16 = (
                        ApiV1ProviderAccountsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_17 = (
                        ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_18 = (
                        ApiV1ProviderAccountsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_19 = (
                        ApiV1ProviderAccountsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_20 = (
                        ApiV1ProviderAccountsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_21 = (
                        ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_22 = (
                        ApiV1ProviderAccountsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_23 = (
                        ApiV1ProviderAccountsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_24 = (
                        ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_25 = (
                        ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_26 = (
                        ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_27 = (
                        ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_28 = (
                        ApiV1ProviderAccountsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_29 = (
                        ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_30 = (
                        ApiV1ProviderAccountsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_31 = (
                        ApiV1ProviderAccountsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_32 = (
                        ApiV1ProviderAccountsArchiveCreateApiKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_33 = (
                        ApiV1ProviderAccountsArchiveCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_34 = (
                        ApiV1ProviderAccountsArchiveCreateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_35 = (
                        ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_36 = (
                        ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_37 = (
                        ApiV1ProviderAccountsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_38 = (
                        ApiV1ProviderAccountsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_archive_create_error_type_39 = (
                        ApiV1ProviderAccountsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_provider_accounts_archive_create_error_type_40 = (
                    ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_provider_accounts_archive_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_provider_accounts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_provider_accounts_archive_create_validation_error.additional_properties = d
        return api_v1_provider_accounts_archive_create_validation_error

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
