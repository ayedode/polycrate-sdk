from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnsrecords_create_annotations_error_component import (
        ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_archived_at_error_component import (
        ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_archived_by_error_component import (
        ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_archived_error_component import (
        ApiV1DomainsDnsrecordsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_archived_reason_error_component import (
        ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_content_error_component import (
        ApiV1DomainsDnsrecordsCreateContentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_created_by_component_error_component import (
        ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_created_by_user_error_component import (
        ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_criticality_error_component import (
        ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_debug_mode_error_component import (
        ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_display_name_error_component import (
        ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_dns_zone_id_error_component import (
        ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_kind_error_component import (
        ApiV1DomainsDnsrecordsCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_labels_error_component import (
        ApiV1DomainsDnsrecordsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_modified_by_user_error_component import (
        ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_name_error_component import (
        ApiV1DomainsDnsrecordsCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_non_field_errors_error_component import (
        ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_platform_service_error_component import (
        ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_priority_error_component import (
        ApiV1DomainsDnsrecordsCreatePriorityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_provider_error_component import (
        ApiV1DomainsDnsrecordsCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_provider_id_error_component import (
        ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_provider_reference_error_component import (
        ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_sla_availability_error_component import (
        ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_sla_target_error_component import (
        ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_sla_window_days_error_component import (
        ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_slo_availability_error_component import (
        ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_slo_target_error_component import (
        ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_slo_window_days_error_component import (
        ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_target_availability_error_component import (
        ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_tolerations_error_component import (
        ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_ttl_error_component import (
        ApiV1DomainsDnsrecordsCreateTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_create_type_error_component import (
        ApiV1DomainsDnsrecordsCreateTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnsrecordsCreateValidationError")


@_attrs_define
class ApiV1DomainsDnsrecordsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent |
            ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent | ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent |
            ApiV1DomainsDnsrecordsCreateArchivedErrorComponent | ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnsrecordsCreateContentErrorComponent | ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent
            | ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent | ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent |
            ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent | ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent |
            ApiV1DomainsDnsrecordsCreateKindErrorComponent | ApiV1DomainsDnsrecordsCreateLabelsErrorComponent |
            ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent | ApiV1DomainsDnsrecordsCreateNameErrorComponent |
            ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent | ApiV1DomainsDnsrecordsCreatePriorityErrorComponent |
            ApiV1DomainsDnsrecordsCreateProviderErrorComponent | ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent |
            ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent | ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent
            | ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent | ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent
            | ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent | ApiV1DomainsDnsrecordsCreateTtlErrorComponent |
            ApiV1DomainsDnsrecordsCreateTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent
        | ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent
        | ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent
        | ApiV1DomainsDnsrecordsCreateArchivedErrorComponent
        | ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnsrecordsCreateContentErrorComponent
        | ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent
        | ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent
        | ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent
        | ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent
        | ApiV1DomainsDnsrecordsCreateKindErrorComponent
        | ApiV1DomainsDnsrecordsCreateLabelsErrorComponent
        | ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnsrecordsCreateNameErrorComponent
        | ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnsrecordsCreatePriorityErrorComponent
        | ApiV1DomainsDnsrecordsCreateProviderErrorComponent
        | ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent
        | ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent
        | ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent
        | ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent
        | ApiV1DomainsDnsrecordsCreateTtlErrorComponent
        | ApiV1DomainsDnsrecordsCreateTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnsrecords_create_annotations_error_component import (
            ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_at_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_by_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_content_error_component import (
            ApiV1DomainsDnsrecordsCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_criticality_error_component import (
            ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_display_name_error_component import (
            ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_kind_error_component import (
            ApiV1DomainsDnsrecordsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_labels_error_component import (
            ApiV1DomainsDnsrecordsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_name_error_component import (
            ApiV1DomainsDnsrecordsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_platform_service_error_component import (
            ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_priority_error_component import (
            ApiV1DomainsDnsrecordsCreatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_id_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_target_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_target_error_component import (
            ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_target_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_tolerations_error_component import (
            ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_ttl_error_component import (
            ApiV1DomainsDnsrecordsCreateTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_type_error_component import (
            ApiV1DomainsDnsrecordsCreateTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnsrecords_create_annotations_error_component import (
            ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_at_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_by_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_content_error_component import (
            ApiV1DomainsDnsrecordsCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_created_by_user_error_component import (
            ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_criticality_error_component import (
            ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_display_name_error_component import (
            ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_kind_error_component import (
            ApiV1DomainsDnsrecordsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_labels_error_component import (
            ApiV1DomainsDnsrecordsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_name_error_component import (
            ApiV1DomainsDnsrecordsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_platform_service_error_component import (
            ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_priority_error_component import (
            ApiV1DomainsDnsrecordsCreatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_id_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_target_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_target_error_component import (
            ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_target_availability_error_component import (
            ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_tolerations_error_component import (
            ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_ttl_error_component import (
            ApiV1DomainsDnsrecordsCreateTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_create_type_error_component import (
            ApiV1DomainsDnsrecordsCreateTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent
                | ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent
                | ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent
                | ApiV1DomainsDnsrecordsCreateArchivedErrorComponent
                | ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnsrecordsCreateContentErrorComponent
                | ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent
                | ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent
                | ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent
                | ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent
                | ApiV1DomainsDnsrecordsCreateKindErrorComponent
                | ApiV1DomainsDnsrecordsCreateLabelsErrorComponent
                | ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnsrecordsCreateNameErrorComponent
                | ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnsrecordsCreatePriorityErrorComponent
                | ApiV1DomainsDnsrecordsCreateProviderErrorComponent
                | ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent
                | ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent
                | ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent
                | ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent
                | ApiV1DomainsDnsrecordsCreateTtlErrorComponent
                | ApiV1DomainsDnsrecordsCreateTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_0 = (
                        ApiV1DomainsDnsrecordsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_1 = (
                        ApiV1DomainsDnsrecordsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_2 = (
                        ApiV1DomainsDnsrecordsCreateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_3 = (
                        ApiV1DomainsDnsrecordsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_4 = (
                        ApiV1DomainsDnsrecordsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_5 = (
                        ApiV1DomainsDnsrecordsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_6 = (
                        ApiV1DomainsDnsrecordsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_7 = (
                        ApiV1DomainsDnsrecordsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_8 = (
                        ApiV1DomainsDnsrecordsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_9 = (
                        ApiV1DomainsDnsrecordsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_10 = (
                        ApiV1DomainsDnsrecordsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_11 = (
                        ApiV1DomainsDnsrecordsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_12 = (
                        ApiV1DomainsDnsrecordsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_13 = (
                        ApiV1DomainsDnsrecordsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_14 = (
                        ApiV1DomainsDnsrecordsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_15 = (
                        ApiV1DomainsDnsrecordsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_16 = (
                        ApiV1DomainsDnsrecordsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_17 = (
                        ApiV1DomainsDnsrecordsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_18 = (
                        ApiV1DomainsDnsrecordsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_19 = (
                        ApiV1DomainsDnsrecordsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_20 = (
                        ApiV1DomainsDnsrecordsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_21 = (
                        ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_22 = (
                        ApiV1DomainsDnsrecordsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_23 = (
                        ApiV1DomainsDnsrecordsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_24 = (
                        ApiV1DomainsDnsrecordsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_25 = (
                        ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_26 = (
                        ApiV1DomainsDnsrecordsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_27 = (
                        ApiV1DomainsDnsrecordsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_28 = (
                        ApiV1DomainsDnsrecordsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_29 = (
                        ApiV1DomainsDnsrecordsCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_30 = (
                        ApiV1DomainsDnsrecordsCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_31 = (
                        ApiV1DomainsDnsrecordsCreateTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_32 = (
                        ApiV1DomainsDnsrecordsCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_33 = (
                        ApiV1DomainsDnsrecordsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_34 = (
                        ApiV1DomainsDnsrecordsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_create_error_type_35 = (
                        ApiV1DomainsDnsrecordsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_create_error_type_36 = (
                    ApiV1DomainsDnsrecordsCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_create_error_type_36

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnsrecords_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnsrecords_create_validation_error.additional_properties = d
        return api_v1_domains_dnsrecords_create_validation_error

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
