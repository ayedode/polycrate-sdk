from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_instances_archive_create_annotations_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_archived_at_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_archived_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_archived_reason_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_config_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_consumer_meta_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_criticality_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_debug_mode_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_deployment_strategy_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_display_name_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_enable_grpc_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_enable_ssl_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_enable_websockets_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_kind_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_labels_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_last_deployment_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_metrics_data_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_name_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_non_field_errors_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_platform_service_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_ports_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_provider_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_provider_id_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_provider_reference_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_reconciliation_enabled_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_session_affinity_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_sla_availability_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_sla_target_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_slo_availability_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_slo_target_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_ssl_redirect_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent,
    )
    from ..models.api_v1_loadbalancers_instances_archive_create_target_availability_error_component import (
        ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersInstancesArchiveCreateValidationError")


@_attrs_define
class ApiV1LoadbalancersInstancesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent |
            ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent
        | ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_instances_archive_create_annotations_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_at_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_reason_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_config_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_consumer_meta_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_criticality_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_debug_mode_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_deployment_strategy_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_display_name_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_grpc_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_ssl_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_websockets_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_kind_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_labels_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_last_deployment_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_name_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_platform_service_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_ports_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_id_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_reference_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_session_affinity_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_sla_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_sla_target_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_slo_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_slo_target_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_ssl_redirect_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_target_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent):
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
        from ..models.api_v1_loadbalancers_instances_archive_create_annotations_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_at_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_archived_reason_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_config_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_consumer_meta_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_criticality_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_debug_mode_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_deployment_strategy_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_display_name_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_grpc_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_ssl_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_enable_websockets_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_kind_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_labels_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_last_deployment_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_metrics_data_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_name_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_non_field_errors_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_platform_service_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_ports_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_id_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_provider_reference_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_session_affinity_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_sla_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_sla_target_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_slo_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_slo_target_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_ssl_redirect_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_loadbalancers_instances_archive_create_target_availability_error_component import (
            ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent
                | ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_0 = (
                        ApiV1LoadbalancersInstancesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_1 = (
                        ApiV1LoadbalancersInstancesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_2 = (
                        ApiV1LoadbalancersInstancesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_3 = (
                        ApiV1LoadbalancersInstancesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_4 = (
                        ApiV1LoadbalancersInstancesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_5 = (
                        ApiV1LoadbalancersInstancesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_6 = (
                        ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_7 = (
                        ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_8 = (
                        ApiV1LoadbalancersInstancesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_9 = (
                        ApiV1LoadbalancersInstancesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_10 = (
                        ApiV1LoadbalancersInstancesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_11 = (
                        ApiV1LoadbalancersInstancesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_12 = (
                        ApiV1LoadbalancersInstancesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_13 = (
                        ApiV1LoadbalancersInstancesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_14 = (
                        ApiV1LoadbalancersInstancesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_15 = (
                        ApiV1LoadbalancersInstancesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_16 = (
                        ApiV1LoadbalancersInstancesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_17 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_18 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_19 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_20 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_21 = (
                        ApiV1LoadbalancersInstancesArchiveCreatePortsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_22 = (
                        ApiV1LoadbalancersInstancesArchiveCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_23 = (
                        ApiV1LoadbalancersInstancesArchiveCreateConsumerMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_24 = (
                        ApiV1LoadbalancersInstancesArchiveCreateEnableSslErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_25 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_26 = (
                        ApiV1LoadbalancersInstancesArchiveCreateEnableWebsocketsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_27 = (
                        ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_28 = (
                        ApiV1LoadbalancersInstancesArchiveCreateSessionAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_29 = (
                        ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_30 = (
                        ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_31 = (
                    ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_instances_archive_create_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_instances_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_instances_archive_create_validation_error.additional_properties = d
        return api_v1_loadbalancers_instances_archive_create_validation_error

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
